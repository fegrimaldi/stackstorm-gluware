from lib import action
import json

class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = json.loads(parameters["blocks"])

        formatted_blocks = []
        for key in self.blocks.keys():
            blocks = self.blocks[key]
            formatted_blocks.append(blocks)

        # Joining the formatted blocks with commas
        result = "[" + ",".join(json.dumps(block) for block in formatted_blocks) + "]"

        return result
