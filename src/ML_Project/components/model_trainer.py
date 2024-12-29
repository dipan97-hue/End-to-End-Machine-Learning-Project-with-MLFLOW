import pandas as pd
from sklearn.linear_model import ElasticNet
import os
from ML_Project import logger
from ML_Project.entity.config_entity import ModelTrainerConfig
import joblib

class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config
    
    def train(self):
        logger.info ("Now Training the Model")
        training = pd.read_csv(self.config.train_path)
        testing = pd.read_csv(self.config.test_path)

        train_x = training.drop([self.config.target_column], axis =1)
        test_x = testing.drop([self.config.target_column], axis =1)
        train_y = training[[self.config.target_column]]
        test_y = testing[[self.config.target_column]]

        lr = ElasticNet(alpha = self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)
        logger.info("Training Completed")

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))

    
