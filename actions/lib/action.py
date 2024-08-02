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

from st2common.runners.base_action import Action
from st2common import log as logging


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.auth = (self.config["username"], self.config["password"])
        self.base_url = self.config["base_url"]
        self.org_id = self.config["org_id"]
