import sys
from lib import action
from lib.webmethod import WebMethod


class GetWorkflows(action.BaseAction):
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
            self.logger.info(
                "GetGluDeviceId", extra={parameters["device_name"]: devices[0]["id"]}
            )
            return devices[0]["id"]
        else:
            self.logger.error(
                "GetGluDeviceId", extra={"msg": "WebMethod's call response was `None`"}
            )
            sys.exit(1)
