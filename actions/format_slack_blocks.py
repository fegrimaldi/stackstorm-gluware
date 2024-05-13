from lib import action
import json

class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]

        # Extracting values regardless of the key
        for key in self.blocks:
            blocks = self.blocks[key]
        return blocks
