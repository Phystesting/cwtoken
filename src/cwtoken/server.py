from flask import Flask, Response, jsonify
from flask_cors import CORS
import threading
import time
from .exceptions import *

class CWBackend:
    def __init__(self, client, **func_interval):
        self.client = client
        self.functions = {}
        self.intervals = {}
        self.data = {key: None for key in func_interval}
        self.last_update = {key: 0 for key in func_interval}
        default_interval = 300
        for key, value in func_interval.items():
            if callable(value):
                self.functions[key] = value
                self.intervals[key] = default_interval
            else:
                func, interval = value
                self.functions[key] = func
                self.intervals[key] = interval
        self.app = Flask(__name__)
        CORS(self.app)
        for key in self.functions.keys():
            endpoint = f"/{key}"
            def make_route(k):
                def route():
                    return jsonify(self.data[k])
                return route
            self.app.route(endpoint,endpoint=f"route_{key}")(make_route(key))
       
        @self.app.route("/overview")   
        def overview():
            return jsonify(self.data)
    
    def update_data(self):
        update_times = {key: time.time() for key in self.intervals}
        while True:
            for key, func in self.functions.items():
                now = time.time()
                if now - self.last_update[key] >= self.intervals[key]:
                    self.last_update[key] = now
                    update_times[key] = now + self.intervals[key]
                    try:
                        self.data[key] = func(self.client)
                    except FetchError as e:
                        if e.status_code() == 401: # Not authorised so token expired or wrong
                            self.client.get_access_token()
                            self.data[key] = func(self.client)
                        else:
                            self.data[key] = f"Error fetching data"
            next_update = min(update_times.values())
            sleep_time = max(1, next_update - time.time())
            time.sleep(sleep_time)

    def run(self,host=None,port=None,debug=True):
        threading.Thread(target=self.update_data, daemon=True).start() 
        self.app.run(debug=debug, use_reloader=False)