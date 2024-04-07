"""Defines a base action class with logging support for inherited objects.

This module provides a class `BaseAction` which inherits from `st2common.runners.base_action.Action`. 
It serves as a base action class with logging support for objects that inherit from it.

Example:
    from st2common.runners.base_action import Action
    from st2common import log as logging

    class BaseAction(Action):
        def __init__(self, config):
            super(BaseAction, self).__init__(config)

            self.glu_auth = (self.config["glu_username"], self.config["glu_password"])
            self.glu_base_url = self.config["glu_base_url"]
            self.org_id = self.config["glu_org_id"]

            self.logger = logging.getLogger(__name__)

Attributes:
    None

Methods:
    __init__(config): Initializes the base action class with configuration parameters and sets up logging.


Version:
    1.0

Author: 
    Fabricio Grimaldi

"""


from st2common.runners.base_action import Action
from st2common import log as logging


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self.glu_auth = (self.config["glu_username"], self.config["glu_password"])
        self.glu_base_url = self.config["glu_base_url"]
        self.org_id = self.config["glu_org_id"]

        self.logger = logging.getLogger(__name__)

