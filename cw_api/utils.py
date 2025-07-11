import requests

def test_connection():
    url = 'https://atukpostgrest.clubwise.com/'
    try:
        response = requests.head(url, timeout=5)
        if response.status_code < 400:
            return True, f"Server is reachable (status code: {response.status_code})"
        else:
            return False, f"Server responded, but with error status code: {response.status_code}"
    except requests.exceptions.ConnectionError:
        return False, "Failed to connect: Server unreachable."
    except requests.exceptions.Timeout:
        return False, f"Connection timed out after {timeout} seconds."
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"