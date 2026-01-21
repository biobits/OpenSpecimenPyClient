# OpenSpecimen Python API Client

A lightweight, Pythonic client for interacting with the OpenSpecimen REST API.  
This library is a clean rewrite of a C# NSwag‑generated client and supports:

- Session authentication (`/sessions`)
- Executing AQL queries (`/query`)
- Modern HTTP handling with `httpx`
- Type‑independent JSON responses
- Easy integration in backend or scripting workflows

Licensed under the MIT License.

---

## Features

- Simple and readable API
- Manage sessions and API tokens
- Execute AQL queries with minimal boilerplate
- Clear error handling with custom exceptions
- Built on the modern `httpx` HTTP client
- Minimal dependencies and easily extensible

---

## Installation

Install the required dependency:

bash
pip install httpx



Add the `client.py` and `api_query.py` files to your project, or package this project and install it via pip.

---

## Project Structure


.
├── client.py        # Low-level HTTP and JSON handling
└── api_query.py     # High-level API wrapper with session handling



---

## Quick Start

Authenticate and run a query

python
from api_query import ApiQuery

session_info = {
    "loginName": "admin",
    "password": "secret",
    "domainName": "openspecimen"
}

api = ApiQuery(
    base_url="https://your.openspecimen.server/openspecimen",
    session_info=session_info
)

query = {
    "aql": "select cp.shortTitle from Participant p",
    "cpId": "123"
}

response = api.execute_query(query)

print(response)



---

## Using the low-level Client class directly

python
from client import Client

client = Client("https://your.openspecimen.server/openspecimen")

session_response = client.set_session({
    "loginName": "admin",
    "password": "secret",
    "domainName": "openspecimen"
})

api_token = session_response["token"]

result = client.execute_query(
    {"aql": "select id from Participant p"},
    api_token
)

print(result)



---

## Error Handling

All non‑200 responses raise an `ApiException`, which includes:

- Status code
- Response body (truncated if large)
- Headers
- Original exception if applicable

Example:

python
try:
    result = api.execute_query(query)
except ApiException as ex:
    print("API Error:", ex)



---

## Roadmap

Planned improvements:

- Optional Pydantic data models for strong typing
- Async client version using `httpx.AsyncClient`
- Packaging on PyPI

---

## Contributing

Contributions, bug reports, and feature requests are welcome.  
Please open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License.  
See the `LICENSE` file for details.

---