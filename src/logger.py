# ---------------------------------------------------
# LOGGING SETUP SCRIPT
# ---------------------------------------------------
# Purpose: This script sets up a logging system so that
# all your program messages (info, errors, warnings)
# are stored in a log file inside a "logs" folder.
# ---------------------------------------------------

import logging         # Python's built-in logging library
import os              # For creating folders & file paths
from datetime import datetime  # For adding timestamp in log filename


# STEP 1: Create a log file name with current date & time
# Example: "08_08_2025_11_45_23.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_H_%M_%S')}.log"

# STEP 2: Create a folder path for logs
# os.getcwd() → current working directory (where you run the script)
# "logs" → folder name
# LOG_FILE → file name
# This creates a path like: "<current_dir>/logs/08_08_2025_11_45_23.log"
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# STEP 3: Make the directory if it doesn't exist
# exist_ok=True → no error if folder already exists
os.makedirs(logs_path, exist_ok=True)

# STEP 4: Create the final log file path
# Now the log file will be inside the folder created above
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# STEP 5: Configure the logging system
# - filename → where logs will be saved
# - format → how logs will look
# - level → log level (INFO means only INFO & above are recorded)
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Optional testing (uncomment to check if logging works)
# if __name__=="__main__":
#     logging.info("Logging has started")