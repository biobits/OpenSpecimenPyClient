import httpx
import json


class ApiException(Exception):
    def __init__(self, message, status, response, headers, inner=None):
        super().__init__(f"{message}\nStatus: {status}\nResponse:\n{response}")
        self.status = status
        self.response = response
        self.headers = headers
        self.inner = inner


class Client:
    def __init__(self, base_url="https://my.openspecimen.net/openspecimen"):
        self.base_url = base_url.rstrip("/")
        self.session = httpx.Client(base_url=self.base_url)
    
    def set_session(self, session_info):
        url = "/sessions"
        resp = self.session.post(url, json=session_info)
        return self._handle_response(resp, dict)

    def execute_query(self, query_info, api_token):
        url = "/query"
        headers = {"X-OS-API-TOKEN": api_token}
        resp = self.session.post(url, json=query_info, headers=headers)
        return self._handle_response(resp, dict)

    def _handle_response(self, resp, expected_type):
        status = resp.status_code
        text = resp.text
        headers = dict(resp.headers)

        if status == 200:
            try:
                return resp.json()
            except json.JSONDecodeError as e:
                raise ApiException("JSON decode failed", status, text, headers, e)
        else:
            raise ApiException("Unexpected status code", status, text, headers)