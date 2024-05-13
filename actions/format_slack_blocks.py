from lib import action
import json


class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = parameters["blocks"]
        blockJson = json.loads(self.blocks)

        formatted_blocks = []
        for block in blockJson:
            formatted_blocks.append(json.dumps(block))

        return formatted_blocks
