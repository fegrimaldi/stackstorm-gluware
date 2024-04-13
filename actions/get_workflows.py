"""Defines an action to retrieve Gluware workflows.

This module provides a class `GetGluWorkflows` which inherits from `action.BaseAction`. 
It enables users to retrieve Gluware workflows based on specified parameters and returns 
information about each workflow,including its name, ID, and the last run timestamp 
converted to UTC string format.

Attributes:
    None

Methods:
    run(**parameters): Executes the action to retrieve Gluware workflows.

Version:
    1.0

Author: 
    Fabricio E. Grimaldi
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
                
                try:
                    descr = workflow["description"]
                except Exception:
                    descr = ""

                result.append({
                    "name": workflow["name"],
                    "description": descr,
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
