"""Defines an action to run a Gluware workflow with provided parameters.

This module provides a class `RunGluWorklflow` which inherits from `action.BaseAction`. 
It enables users to run a Gluware workflow with provided parameters.

Example:
    from lib import action
    from lib.webmethod import WebMethod

    class RunGluWorklflow(action.BaseAction):
        def run(self, **parameters):
            self.web_method = WebMethod(verify=False)
            response_raw = self.web_method.call(
                method="POST",
                url=f"{self.glu_base_url}/api/workflows/{parameters["workflow_id"]}/run",
                json={
                    "orgId": self.org_id,
                    "deviceIds": [parameters["device_id"]],
                    "inputParameters": {},
                },
                headers=None,
                auth=self.glu_auth,
            )
            if response_raw is not None:
                return response_raw.status_code
            else:
                return {"status": "unhandled exception"}

Attributes:
    None

Methods:
    run(**parameters): Executes the action to run a Gluware workflow with provided parameters.

Version:
    1.0

Author: 
    Fabricio Grimaldi

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
            url=f"{self.glu_base_url}/api/workflows/{workflow_id}/run",
            json={
                "orgId": self.org_id,
                "deviceIds": [parameters["device_id"]],
                "inputParameters": {},
            },
            headers=None,
            auth=self.glu_auth,
        )
        if response is not None:
            self.logger.info("RunGluWorkFlow", extra={"msg": f"WebMethod's call response: {response.status_code}"})
            return response.status_code
        else:
            self.logger.error("RunGluWorkFlow", extra={"msg": "WebMethod's call response: None"})
            sys.exit(1)
