"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   Copyright 2024 Silver Wolf Technology
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

    def call(self, method, url, params=None, json=None, data=None, headers=None, auth=None):
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
                    url, data=data, headers=headers, auth=auth, verify=self.verify
                )
            elif method == "DELETE":
                response = requests.delete(
                    url, headers=headers, auth=auth, verify=self.verify
                )
            response.raise_for_status()
        except (requests.exceptions.HTTPError, 
                requests.exceptions.ConnectionError, 
                requests.exceptions.Timeout, 
                requests.exceptions.RequestException) as err:
            self.logger.error(f"WebMethod: {method}. Error: {err}")
            sys.exit(1)
        except Exception as e:
            self.logger.error(f"General Exception: {e}")
            sys.exit(1)

        self.logger.info(f"Success. WebMethod: {method}. Response: {response.status_code}")
        return response
