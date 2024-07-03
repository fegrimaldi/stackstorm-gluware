"""Updates the CVE summary for all devices in the Gluware platform.

This script provides a class `UpdateCveSummary` which inherits from `action.BaseAction`. 
It enables users to update the CVE summary for all devices by retrieving device information,
aggregating CVE advisories, and sending the updated information back to Gluware.

Attributes:
    None

Methods:
    run(**parameters): Executes the action to update the CVE summary for all devices.

Version:
    1.0

Author: 
    Fabricio E. Grimaldi
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
