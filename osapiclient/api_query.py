
import pandas as pd

from .client import Client


class ApiQuery:
    """
    A wrapper class for executing queries on the OpenSpecimen API.

    Handles session management and query execution.
    """

    def __init__(self, base_url=None, session_info=None):
        """
        Initialize the ApiQuery instance.

        Args:
            base_url: Optional base URL for the API client
            session_info: Optional session info to authenticate immediately
        """
        self.client = Client(base_url) if base_url else Client()
        self.session_token = None

        if session_info:
            result = self.client.set_session(session_info)
            self.session_token = result.get("token")

    def set_session(self, session_info):
        """
        Set the session and store the token.

        Args:
            session_info: Dict with login credentials

        Returns:
            Session response dict
        """
        result = self.client.set_session(session_info)
        self.session_token = result.get("token")
        return result

    def execute_query(self, query_info, api_token=None):
        """
        Execute a query using the stored or provided token.

        Args:
            query_info: Dict with query details
            api_token: Optional API token; uses stored token if not provided

        Returns:
            Query results dict

        Raises:
            ValueError: If no token is available
        """
        token = api_token or self.session_token
        if not token:
            raise ValueError("No API token available. Authenticate first.")
        return self.client.execute_query(query_info, token)

    def execute_query_as_dataframe(self, query_info, api_token=None):
        """
        Execute a query and return results as a pandas DataFrame.

        Args:
            query_info: Dict with query details
            api_token: Optional API token; uses stored token if not provided

        Returns:
            pandas.DataFrame with query results

        Raises:
            ValueError: If no token is available
            KeyError: If response doesn't contain expected fields
        """
        response = self.execute_query(query_info, api_token)

        # Extract the data from the response
        rows = response.get('rows', [])
        column_labels = response.get('columnLabels', [])

        # Create DataFrame
        df = pd.DataFrame(rows, columns=column_labels)

        return df
