import json
from st2common.runners.base_action import Action

class SaveJsonToDisk(Action):
    def run(self, **parameters):
        try:
            with open(parameters["file_path"], 'w') as f:
                json.dump(parameters["payload"], f, indent=4)
            self.logger.info(f"Payload saved to {parameters["file_path"]}")
            return True, f"Payload saved to {parameters["file_path"]}"
        except Exception as e:
            self.logger.error(f"Failed to save payload: {str(e)}")
            return False, f"Failed to save payload: {str(e)}"
