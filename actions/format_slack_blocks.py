from lib import action
import json

class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = json.loads(parameters["blocks"])

        for key in self.blocks.keys():
            blocks = self.blocks[key]
            return blocks

