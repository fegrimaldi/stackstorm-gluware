from lib import action
import json

class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]

        # Extracting values regardless of the key
        formatted_blocks = list(self.blocks.values())

        return formatted_blocks
