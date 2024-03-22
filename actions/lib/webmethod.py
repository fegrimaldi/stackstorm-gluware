import sys
import requests
from requests.exceptions import HTTPError, RequestException
from urllib3.exceptions import InsecureRequestWarning


class WebMethod:

    def __init__(self, verify=True):
        if not verify:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        self.verify = verify

    def call(self, method, url, params=None, payload=None, headers=None, auth=None):
        """
        Calls the specified HTTP method (GET, POST, PATCH, etc.) using the requests library.

        Args:
            method (str): The HTTP method to use (GET, POST, PATCH, etc.).
            url (str): The URL to which the request will be sent.
            params (dict, optional): Parameters to be sent in the URL query string (for methods like GET).
            headers (dict, optional): Headers to be included in the request.
            payload (dict, optional): Data to be sent in the request body (for methods like POST and PATCH).
            auth (tuple, optional): (username, password) tuple for basic authentication.

        Returns:
            requests.Response: Response object returned by the HTTP request.
        """

        method = method.upper()
        if method not in ["GET", "POST", "PATCH", "PUT", "DELETE"]:
            print(
                "Invalid HTTP method. Allowed methods are GET, POST, PATCH, PUT, DELETE."
            )
            sys.exit(1)

        try:
            if method == "GET":
                response = requests.get(
                    url, params=params, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "POST":
                response = requests.post(
                    url, json=payload, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "PATCH":
                response = requests.patch(
                    url, json=payload, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "PUT":
                response = requests.put(
                    url, json=payload, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "DELETE":
                response = requests.delete(
                    url, headers=headers, auth=auth, verify=self.verify
                )
            response.raise_for_status()
        except (HTTPError, RequestException) as err:
            print(err)
            sys.exit(1)

        return response
