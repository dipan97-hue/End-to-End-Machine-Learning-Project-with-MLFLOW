from ML_Project import logger
from ML_Project.components.data_transformation import DataTransformation
from ML_Project.config.configuration import ConfigurationManager
import pandas as pd
from pathlib import Path

STAGE_NAME = "DATA TRANSFORMATION"

class DataTransformationPipeline:
    def __init__(self):
        pass
    @staticmethod
    def main():
        try:
            with open(r'D:\exercises\Cold_Email_Generator\MLOPS\End-to-End-Machine-Learning-Project-with-MLFLOW\artifacts\data_validation\status.txt', 'r') as f:
                status = f.read().split(":")[-1]
                # print(status)

            if status == "True":

                config = ConfigurationManager()
                data_config = config.get_data_transformation_config()
                data_transformer = DataTransformation(data_config)
                data_transformer.train_test_splittting()
            else:
                logger.info("Data Validation is not completed")
        except Exception as e:
            logger.error(f"Error in Data Transformation: {str(e)}")
            raise e

if __name__ == "__main__":
    try:
        logger.info(f"Transformation Started {STAGE_NAME}")
        pipeline = DataTransformationPipeline()
        pipeline.main()
        logger.info(f"Transformation Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Error in the Transformation")
        raise e