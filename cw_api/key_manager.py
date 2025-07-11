import requests
import pandas as pd

base_url = 'https://atukpostgrest.clubwise.com/'

def get_access_token(clubcode, api_token,timeout=10):
    request_url = base_url + 'access-token'
    request_header = {
        'CW-API-Token': api_token,
        'Content-Type': 'application/json'
    }
    request_payload = {'sClubCode': clubcode}

    try:
        response = requests.post(request_url, json=request_payload, headers=request_header, timeout=timeout)
        response.raise_for_status()  # Raises HTTPError on bad status
        my_token = response.json().get('access-token')
        if not my_token:
            print("Access token not found in response. Check your club code and API token.")
            return None
        return my_token
    except requests.exceptions.RequestException as e:
        print(f"Error generating access token: {e}")
        return None

def fetch(clubcode, api_token, url, timeout=10):
    my_token = get_access_token(clubcode, api_token, timeout)
    if not my_token:
        print("\nFailed to fetch access token. Aborting.\nTry running test_connection() or double-check your club code and static token.\n")
        return None  # Stops function execution here if token failed

    access_headers = {
        'CW-API-Token': api_token,
        'Authorization': f'Bearer {my_token}'
    }
    combined_url = base_url + url

    try:
        response = requests.get(combined_url, headers=access_headers)
        response.raise_for_status()
        data = response.json()
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
