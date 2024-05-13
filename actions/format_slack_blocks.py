from lib import action
import json


class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]
        blockJson = json.loads(self.blocks)

        formatted_blocks = {}
        for key, blocks in blockJson.items():
            formatted_blocks[key] = json.dumps(blocks)

        return formatted_blocks
