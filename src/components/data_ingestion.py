import sys, os
# sys and os are used for file path handling and system operations

# This adds the parent directory of the current file to Python's import path
# so we can import modules from the src folder.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import sys
import os
from src.exception import CustomException  # Custom error handling
from src.logger import logging             # Logging setup
import pandas as pd                        # For working with CSV files
from sklearn.model_selection import train_test_split  # For splitting data
from dataclasses import dataclass           # To create a class for configuration

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# -------------------------
# CONFIGURATION CLASS
# -------------------------
@dataclass # it is a decorator
class DataIngestionConfig:
    """
    This class holds the file paths where the raw, train, 
    and test CSV files will be stored. Gives  input to the data ingestion...
    """
    train_data_path = os.path.join('artifacts', 'train.csv')
    test_data_path = os.path.join('artifacts', 'test.csv')
    raw_data_path = os.path.join('artifacts', 'data.csv')

# -------------------------
# MAIN DATA INGESTION CLASS
# -------------------------
class DataIngestion:
    """
    Reads data from a source, saves it in 'artifact' folder,
    and splits into train and test CSV files.
    """
    def __init__(self):
        # Create an object of DataIngestionConfig to access file paths
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        """
        Reads CSV data, saves raw data, splits into train/test sets,
        and saves them into the 'artifact' folder.
        """
        logging.info("Entered the data ingestion method or component")

        try:
            # Step 1: Read dataset from local file
            df = pd.read_csv(r'notebook\data\stud.csv')
            logging.info("Read the dataset as dataframe")

            # Step 2: Create the 'artifact' folder if it doesn't exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Save the raw dataset
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Step 4: Train-test split
            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Save train and test datasets
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of the data is completed')

            # Step 6: Return paths for further processing (e.g., Data Transformation)
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # If error occurs, wrap it in CustomException
            raise CustomException(e, sys)


# -------------------------
# SCRIPT EXECUTION
# -------------------------
if __name__ == "__main__":
    obj = DataIngestion()  # Create DataIngestion object
    train_data, test_data = obj.initiate_data_ingestion()  # Run ingestion process
    print("Train CSV saved at:", train_data)
    print("Test CSV saved at:", test_data)

 # Now combined transformation to this ingestion
    data_transformation=DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)

# -------------------------------------------------------------------------------------
#  -m Flag Ka Magic
# Jab tum command me -m lagate ho, to Python usko module ke roop me samajhta hai, aur automatically tumhare project root folder ko import path me add kar deta hai.

# Matlab, jab tum karte ho:
# Run python -m src.components.data_ingestion
