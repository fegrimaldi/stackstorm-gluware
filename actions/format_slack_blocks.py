from lib import action
import json


class GetBgpState(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]

        for key in self.blocks.keys():
            blocks = self.blocks[key]
            blockDump = json.dumps(blocks)

        return json.dumps(blockDump)
