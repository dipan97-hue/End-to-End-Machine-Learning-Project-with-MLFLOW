from ML_Project import logger
from ML_Project.components.data_validation import DataValidation
from ML_Project.config.configuration import ConfigurationManager
import pandas as pd

STAGE_NAME = "DATA VALIDATION"

class DataValidationPipeline:
    def __init__(self):
        pass
    @staticmethod
    def main():
        config = ConfigurationManager()
        data_config = config.get_data_validation_config()
        data_validator = DataValidation(data_config)
        data_validator.validate_all()

if __name__ == "__main__":
    try:
        logger.info(f"Stagging Started {STAGE_NAME}")
        pipeline = DataValidationPipeline()
        pipeline.main()
        logger.info(f"Stagging Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Error in the Stagging")
        raise e