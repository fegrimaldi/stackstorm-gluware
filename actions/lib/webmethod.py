"""Defines a class for making HTTP requests using the requests library with logging support.

This module provides a class `WebMethod` for making HTTP requests using the `requests` library. 
It includes methods for various HTTP methods such as GET, POST, PATCH, PUT, and DELETE. 
The class also supports logging using the `st2common.log` module.

Example:
    import sys
    import requests
    from requests.exceptions import HTTPError, RequestException
    from urllib3.exceptions import InsecureRequestWarning
    from st2common import log as logging

    class WebMethod:

        def __init__(self, verify=True):
            if not verify:
                requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
            self.verify = verify
            self.logger = logging.getLogger(__name__)

        def call(self, method, url, params=None, json=None, headers=None, auth=None):
      
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
        
            method = method.upper()
            if method not in ["GET", "POST", "PATCH", "PUT", "DELETE"]:
                print(
                    "Invalid HTTP method. Allowed methods are GET, POST, PATCH, PUT, DELETE."
                )
                self.logger.error(f"Invalid HTTP method: {method}")
                sys.exit(1)

            try:
                if method == "GET":
                    response = requests.get(
                        url, params=params, headers=headers, auth=auth, verify=self.verify
                    )
                elif method == "POST":
                    response = requests.post(
                        url, json=json, headers=headers, auth=auth, verify=self.verify
                    )
                elif method == "PATCH":
                    response = requests.patch(
                        url, json=json, headers=headers, auth=auth, verify=self.verify
                    )
                elif method == "PUT":
                    response = requests.put(
                        url, json=json, headers=headers, auth=auth, verify=self.verify
                    )
                elif method == "DELETE":
                    response = requests.delete(
                        url, headers=headers, auth=auth, verify=self.verify
                    )
                response.raise_for_status()
            except (HTTPError, RequestException) as err:
                self.logger.error(err)
                sys.exit(1)

            self.logger.info(f"WebMethod: {method} completed successfully")
            return response

Attributes:
    None

Methods:
    __init__(verify=True): Initializes the WebMethod object with the specified verification settings and sets up logging.
    call(method, url, params=None, json=None, headers=None, auth=None): Makes an HTTP request using the specified method 
    and parameters, with logging support.

Version:
    1.0

Author: 
    Fabricio Grimaldi

"""

import sys
import requests
from requests.exceptions import HTTPError, RequestException
from urllib3.exceptions import InsecureRequestWarning
from st2common import log as logging


class WebMethod:

    def __init__(self, verify=True):
        if not verify:
            requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
        self.verify = verify
        self.logger = logging.getLogger(__name__)

    def call(self, method, url, params=None, json=None, headers=None, auth=None):
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
            self.logger.ERROR(f"Invalid HTTP method: {method}")
            sys.exit(1)

        try:
            if method == "GET":
                response = requests.get(
                    url, params=params, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "POST":
                response = requests.post(
                    url, json=json, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "PATCH":
                response = requests.patch(
                    url, json=json, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "PUT":
                response = requests.put(
                    url, json=json, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "DELETE":
                response = requests.delete(
                    url, headers=headers, auth=auth, verify=self.verify
                )
            response.raise_for_status()
        except (HTTPError, RequestException) as err:
            self.logger.ERROR(f"WebMethod: {method}", extra={"msg": err})
            sys.exit(1)

        self.logger.INFO(
            f"WebMethod: {method}", extra={"msg": "Success"}
        )
        return response
