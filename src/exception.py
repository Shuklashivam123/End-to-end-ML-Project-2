import sys # Used to get exception details like type, file name, line number
import logging
from src.logger import logging  # Importing our custom logger configuration


# ---------------------------------------------------
# FUNCTION: error_message_detail
# ---------------------------------------------------
# Purpose: This function creates a detailed error message
# that includes the file name, line number, and the actual error.
# ---------------------------------------------------
def error_message_detail(error, error_detail: sys):
    # exc_info() returns (type, value, traceback)
    # We only need the traceback object (exc_tb)
    _, _, exc_tb = error_detail.exc_info()  # exc_tb = traceback object containing error location

    # Get the filename from the traceback object
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a custom formatted error message
    error_message = "Error Occured in python script name [{0}] line number [{1}] error message [{2}] ".format(
        file_name,  # Script where the error occurred
        exc_tb.tb_lineno,  # Line number where error happened
        str(error)  # Original error message
    )

    return error_message  # Send this message back to be displayed/logged


# ---------------------------------------------------
# CLASS: CustomException
# ---------------------------------------------------
# Purpose: Our own exception class that overrides the
# default Python Exception to include detailed info.
# ---------------------------------------------------
class CustomException(Exception):  # Inherits from Python's built-in Exception
    def __init__(self, error_message, error_detail: sys):  # Constructor
        # Call the base class constructor
        super().__init__(error_message)

        # Replace normal message with detailed message from error_message_detail()
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):  # This method is called when the object is printed or converted to string
        return self.error_message


# ---------------------------------------------------
# TESTING THE CUSTOM EXCEPTION
# ---------------------------------------------------
if __name__ == "__main__":

    try:
        1 / 0  # This will cause a ZeroDivisionError
    except Exception as e:
        logging.info("Divide by Zero Error!")  # Log info message
        # Raise our CustomException instead of normal Exception
        raise CustomException(e, sys)