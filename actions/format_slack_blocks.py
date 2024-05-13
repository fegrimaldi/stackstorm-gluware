from lib import action
import json

class FormatSlackBlocks(action.BaseAction):
    def run(self, **parameters):
        self.blocks = json.loads(parameters["blocks"])

        formatted_blocks = []
        for block in self.blocks:
            formatted_blocks.append(json.dumps(block))

        # Joining the formatted blocks with commas
        result = "[" + ",".join(formatted_blocks) + "]"

        return result
