from st2common.runners.base_action import Action
import os

class SaveCsvToDisk(Action):

    def run(self, **parameters):
        file_path = parameters["file_path"]
        data = parameters["data"]

        # Ensure data is in the correct format
        if not isinstance(data, str):
            self.logger.error("Data is not a string")
            return False

        try:
            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(data)
            
            self.logger.info(f"CSV data saved to {file_path}")
            return file_path
        except Exception as e:
            self.logger.error(f"Failed to save payload: {str(e)}")
            return False
