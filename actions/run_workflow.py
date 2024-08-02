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


class RunGluWorklflow(action.BaseAction):
    def run(self, **parameters):
        workflow_id = parameters["workflow_id"]

        self.web_method = WebMethod(verify=False)

        response = self.web_method.call(
            method="POST",
            url=f"{self.base_url}/api/workflows/{workflow_id}/run",
            json={
                "orgId": self.org_id,
                "deviceIds": parameters["device_ids"],
                "inputParameters": parameters["input_params"],
            },
            headers=None,
            auth=self.auth,
        )
        if response is not None:
            self.logger.info(f"WebMethod's call response: {response.status_code}")
            return response.status_code
        else:
            self.logger.error("WebMethod's call response: None")
            sys.exit(1)

