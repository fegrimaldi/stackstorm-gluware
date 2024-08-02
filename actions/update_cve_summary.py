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
import json
from lib import action
from lib.webmethod import WebMethod


class UpdateCveSummary(action.BaseAction):
    def run(self, **parameters):
        headers = {"Content-Type": "application/json"}
        self.web_method = WebMethod(verify=False)

        # * Get All Cisco Devices
        devices = self.web_method.call(
            method="GET",
            url=f"{self.base_url}/api/devices",
            params={"orgId": self.org_id, "discoveredVendor": "Cisco"},
            json=None,
            headers=None,
            auth=self.auth,
        ).json()

        try:
            # * Loop Through and update all devices
            for dev in devices: 
                deviceId = dev["id"]
                if "discoveredSku" in dev.keys():
                    skuString = dev["discoveredSku"]
                else:
                    skuString = "undiscovered"

                if (dev["accessStatus"] != "UNKNOWN") & (skuString != "undiscovered"):
                    # * Get All Devices
                    device = self.web_method.call(
                        method="GET",
                        url=f"{self.base_url}/api/devices/{deviceId}",
                        params={"orgId": self.org_id},
                        json=None,
                        headers=None,
                        auth=self.auth,
                    ).json()

                    cve_payload = {"id": deviceId}
                    if "Medium Advisories" in device.keys():
                        cve_payload["adv_med"] = device["Medium Advisories"]
                    if "High Advisories" in device.keys():
                        cve_payload["adv_high"] = device["High Advisories"]
                    if "Critical Advisories" in device.keys():
                        cve_payload["adv_crit"] = device["Critical Advisories"]

                    response = self.web_method.call(
                        method="PUT",
                        url=f"{self.base_url}/api/devices/{deviceId}",
                        data=json.dumps(cve_payload),
                        headers=headers,
                        auth=self.auth,
                    )
            return True, "Updated CVE Summaries"
        except Exception as e:
            self.logger.error(f"Error: {e}")
            return False, f"Failed to update CVE Summaries - Error: {e}"
