

import sys
from lib import action
from lib.webmethod import WebMethod

from datetime import datetime, timezone


def js_timestamp_to_utc_string(timestamp):
    # Convert milliseconds to seconds
    seconds = timestamp / 1000
    date_obj = datetime.fromtimestamp(seconds, timezone.utc)
    utc_string = date_obj.strftime('%Y-%m-%d %H:%M:%S UTC')
    return utc_string


class GetGluWorkflows(action.BaseAction):
    def run(self, **parameters):
        self.web_method = WebMethod(verify=False)

        response = self.web_method.call(
            method="GET",
            url=f"{self.glu_base_url}/api/workflows",
            params={
                "orgId": self.org_id,
                "workflowType": "PRODUCTION",
                "private": False
            },
            json=None,
            headers=None,
            auth=self.glu_auth,
        )
        if response is not None:
            result = []
            workflows = response.json()
            for workflow in workflows:
                result.append({
                    "name": workflow["name"],
                    "id":  workflow["id"],
                    "lastRun": js_timestamp_to_utc_string(workflow["lastRun"])
                }) 
            self.logger.info(
                "GetGluWorkflows", extra={"result": result}
            )
            return result
        else:
            self.logger.error(
                "GetGluWorkflows", extra={"msg": "WebMethod's call response was `None`"}
            )
            sys.exit(1)
