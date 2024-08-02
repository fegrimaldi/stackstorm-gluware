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

from datetime import datetime, timezone


def js_timestamp_to_utc_string(timestamp):
    """
    Convert a JavaScript timestamp to a string representing the corresponding UTC datetime.

    Args:
        timestamp (int): The JavaScript timestamp to convert.

    Returns:
        str: A string representing the corresponding UTC datetime in the format 'YYYY-MM-DD HH:MM:SS UTC'.
    """
    seconds = timestamp / 1000
    date_obj = datetime.fromtimestamp(seconds, timezone.utc)
    utc_string = date_obj.strftime("%Y-%m-%d %H:%M:%S UTC")
    return utc_string


class GetGluWorkflows(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod(verify=False)

        response = self.web_method.call(
            method="GET",
            url=f"{self.base_url}/api/workflows",
            params={
                "orgId": self.org_id,
                "workflowType": "PRODUCTION",
                "private": False,
            },
            json=None,
            headers=None,
            auth=self.auth,
        )
        if response is not None:
            result = []
            workflows = response.json()
            for workflow in workflows:

                try:
                    descr = workflow["description"]
                    last_run = workflow["lastRun"]
                except Exception:
                    descr = ""
                if workflow["lastRun"]:
                    last_run = js_timestamp_to_utc_string(workflow["lastRun"])
                else:
                    last_run = "Never"
                result.append(
                    {
                        "name": workflow["name"],
                        "description": descr,
                        "id": workflow["id"],
                        "lastRun": last_run,
                    }
                )
            self.logger.info("Successfully retrieved all public [g]luware workflows.")
            return result
        else:
            self.logger.error("faled to retrieve [g]luware workflows")
            sys.exit(1)
