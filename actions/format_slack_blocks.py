from lib import action
import json


class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]
        blockJson = json.loads(self.blocks)

        for key in blockJson.keys():
            blocks = blockJson[key]
            blockDump = json.dumps(blocks)

        return json.dumps(blockDump)
