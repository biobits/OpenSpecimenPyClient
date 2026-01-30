
import json

import httpx


class ApiException(Exception):
    """
    Custom exception for API errors.

    Attributes:
        status: HTTP status code
        response: Response text
        headers: Response headers
        inner: Inner exception if any
    """

    def __init__(self, message, status, response, headers, inner=None):
        """
        Initialize the exception.

        Args:
            message: Error message
            status: HTTP status code
            response: Response text
            headers: Response headers dict
            inner: Optional inner exception
        """
        super().__init__(f"{message}\nStatus: {status}\nResponse:\n{response}")
        self.status = status
        self.response = response
        self.headers = headers
        self.inner = inner


class Client:
    """
    Client for interacting with OpenSpecimen API.
    """

    def __init__(self, base_url="https://my.openspecimen.net/openspecimen"):
        """
        Initialize the client.

        Args:
            base_url: Base URL of the OpenSpecimen instance
        """
        # Default route to OpenSpecimen Api ist "baseurl/rest/ng"
        apiurl = "/rest/ng"
        self.base_url = f"{base_url.rstrip("/")}{apiurl}"
        self.session = httpx.Client(base_url=self.base_url)

    def set_session(self, session_info):
        """
        Set the session with login credentials.

        Args:
            session_info: Dict with login info

        Returns:
            Session data as dict
        """
        url = "/sessions"
        resp = self.session.post(url, json=session_info)
        return self._handle_response(resp, dict)

    def execute_query(self, query_info, api_token):
        """
        Execute a query on the API.

        Args:
            query_info: Dict with query details
            api_token: API token for authentication

        Returns:
            Query results as dict
        """
        url = "/query"
        headers = {"X-OS-API-TOKEN": api_token}
        resp = self.session.post(url, json=query_info, headers=headers)
        return self._handle_response(resp, dict)

    def _handle_response(self, resp, expected_type):
        """
        Handle HTTP response, parse JSON or raise exception.

        Args:
            resp: httpx.Response object
            expected_type: Expected return type (not used currently)

        Returns:
            Parsed JSON data

        Raises:
            ApiException: On error or invalid JSON
        """
        status = resp.status_code
        text = resp.text
        headers = dict(resp.headers)

        if status == 200:
            try:
                return resp.json()
            except json.JSONDecodeError as e:
                raise ApiException("JSON decode failed",
                                   status, text, headers, e)
        else:
            raise ApiException("Unexpected status code", status, text, headers)
