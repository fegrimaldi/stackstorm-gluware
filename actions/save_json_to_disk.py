import json
from st2common.runners.base_action import Action

class SaveJsonToDisk(Action):
    """
    A StackStorm action that saves a JSON payload posted to a webhook
    to a specified directory on the StackStorm server.

    Methods
    -------
    run(**parameters)
        Saves the JSON payload to the specified file path.

    Parameters
    ----------
    file_path : str
        The path where the JSON payload should be saved.
    payload : dict
        The JSON payload to be saved.

    Returns
    -------
    tuple
        A tuple containing a boolean status and a message. The status is
        True if the payload was saved successfully, otherwise False. The
        message provides additional information about the operation.
    """
    def run(self, **parameters):
        """
        Saves the provided JSON payload to the specified file path.

        Parameters
        ----------
        **parameters : dict
            A dictionary containing the file path and payload.

        Returns
        -------
        tuple
            A tuple containing a boolean status and a message. The status is
            True if the payload was saved successfully, otherwise False. The
            message provides additional information about the operation.
        """
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
