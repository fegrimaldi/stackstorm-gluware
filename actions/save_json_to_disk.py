import json
from st2common.runners.base_action import Action

class SaveJsonToDisk(Action):
    def run(self, **parameters):
        file_path = parameters["file_path"]
        payload = parameters["payload"]
        try:
            with open(file_path, 'w') as f:
                json.dump(payload, f, indent=4)
            self.logger.info(f"Payload saved to {file_path}")
            return True, f"Payload saved to {file_path}"
        except Exception as e:
            self.logger.error(f"Failed to save payload: {str(e)}")
            return False, f"Failed to save payload: {str(e)}"
