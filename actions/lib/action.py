"""Defines a base action class for accessing Gluware APIs with authentication credentials and base URL.

This module provides a class `BaseAction` which inherits from `st2common.runners.base_action.Action`. 
It serves as a base action for accessing Gluware APIs with authentication credentials and base URL.

Example:
    from st2common.runners.base_action import Action

    class BaseAction(Action):
        def __init__(self, config):
            super(BaseAction, self).__init__(config)
            self.glu_auth = (self.config["glu_username"], self.config["glu_password"])
            self.glu_base_url = self.config["glu_base_url"]
            self.org_id = self.config["glu_org_id"]

Attributes:
    None

Methods:
    __init__(config): Initializes the base action class with Gluware authentication credentials and base URL.

"""


from st2common.runners.base_action import Action


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)

        self.glu_auth = (self.config["glu_username"], self.config["glu_password"])
        self.glu_base_url = self.config["glu_base_url"]
        self.org_id = self.config["glu_org_id"]
