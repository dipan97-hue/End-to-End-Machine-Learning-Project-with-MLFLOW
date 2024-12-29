import pandas as pd
from sklearn.linear_model import ElasticNet
import os
from ML_Project import logger
from ML_Project.config.configuration import ConfigurationManager
from ML_Project.entity.config_entity import ModelTrainerConfig
from ML_Project.components.model_trainer import ModelTrainer
import joblib


STAGE_NAME = "MODEL TRAINING"

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(model_trainer_config)
            model_trainer.train()
        except Exception as e:
            logger.error(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f"Training Started {STAGE_NAME}")
        pipeline = ModelTrainerPipeline()
        pipeline.main()
        logger.info(f"Training Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Error in the Training")
        raise e