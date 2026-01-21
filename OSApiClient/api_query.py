from client import Client


class ApiQuery:
    def __init__(self, base_url=None, session_info=None):
        self.client = Client(base_url) if base_url else Client()
        self.session_token = None

        if session_info:
            result = self.client.set_session(session_info)
            self.session_token = result.get("token")

    def set_session(self, session_info):
        result = self.client.set_session(session_info)
        self.session_token = result.get("token")
        return result

    def execute_query(self, query_info, api_token=None):
        token = api_token or self.session_token
        if not token:
            raise ValueError("No API token available. Authenticate first.")
        return self.client.execute_query(query_info, token)