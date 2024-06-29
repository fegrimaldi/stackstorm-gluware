"""Defines an action to retrieve the Gluware device ID by name.

This module provides a class `GetGluDeviceId` which inherits from `action.BaseAction`. 
It enables users to retrieve the Gluware device ID by providing the device name.

Example:
    import sys
    from lib import action
    from lib.webmethod import WebMethod

    class GetGluDeviceId(action.BaseAction):
        def run(self, **parameters):
            self.web_method = WebMethod(verify=False)
            response = self.web_method.call(
                method="GET",
                url=f"{self.glu_base_url}/api/devices",
                params={
                    "orgId": self.org_id,
                    "name": parameters["device_name"],
                },
                json=None,
                headers=None,
                auth=self.glu_auth,
            )
            if response is not None:
                devices = response.json()
                return devices[0]["id"]
            else:
                sys.exit(1)

Attributes:
    None

Methods:
    run(**parameters): Executes the action to retrieve the Gluware device ID by name.

Version:
    1.0

Author: 
    Fabricio Grimaldi
    
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
            self.logger.info(
                "GetGluDeviceId", extra={parameters["device_name"]: devices[0]["id"]}
            )
            return devices[0]["id"]
        else:
            self.logger.error(
                "GetGluDeviceId", extra={"msg": "WebMethod's call response was `None`"}
            )
            sys.exit(1)
