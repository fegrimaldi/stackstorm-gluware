import sys
from lib import action
from lib.webmethod import WebMethod


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
            workflows = response.json()
            self.logger.info(
                "GetGluWorkflows", extra={}
            )
            return workflows
        else:
            self.logger.error(
                "GetGluWorkflows", extra={"msg": "WebMethod's call response was `None`"}
            )
            sys.exit(1)
