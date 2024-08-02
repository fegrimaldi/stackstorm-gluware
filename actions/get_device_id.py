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
from lib import action
from lib.webmethod import WebMethod


class GetGluDeviceId(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod(verify=False)

        response = self.web_method.call(
            method="GET",
            url=f"{self.base_url}/api/devices",
            params={
                "orgId": self.org_id,
                "name": parameters["device_name"],
            },
            json=None,
            headers=None,
            auth=self.auth,
        )
        if response is not None:
            devices = response.json()
            if devices:
                self.logger.info(f"Successfully retrieved device id: {devices[0]["id"]}")
                return devices[0]["id"]
            else:
                self.logger.warning("Could not find device.")
                return None
        else:
            self.logger.error("WebMethod's call response was `None`")
            sys.exit(1)
