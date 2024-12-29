import os
from ML_Project import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from ML_Project.entity.config_entity import DataTrasnformationConfig

class DataTransformation:
    def __init__(self, config: DataTrasnformationConfig):
        self.config = config

    def train_test_splittting(self):
        data = pd.read_csv(self.config.data_file)

        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index = False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index = False)

        logger.info(" Data Transformation Completed")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
