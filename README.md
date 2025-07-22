# cwtoken

cwtoken simplifies working with PostgREST APIs by:

- Automatically handling **access token generation**
- Making authenticated **GET requests** to PostgREST endpoints
- Providing a **CLI** for quick testing and usage
- Including a user-friendly **GUI** for building and running queries without code

---

## Available Functions

### fetch(clubcode, token, request, timeout=10)

Authenticates and executes a GET request to a PostgREST API. Returns a Pandas DataFrame.

---

### get_access_token(clubcode, token, timeout=10)

Returns a fresh access token using your static API token. Use this if you want manual control.

---

### test_connection()

Pings the API server to check if it's reachable.

Can be run from the CLI:

cwtoken test-connection

### cwtoken gui
Launches the graphical interface for building and executing queries with no coding required.

Run it from the CLI like this:

cwtoken gui