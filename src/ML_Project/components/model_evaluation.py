import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from ML_Project.utils.common import read_yaml, create_directories, save_json
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from ML_Project import logger
from ML_Project.config.configuration import ModelEvaluationConfig
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    
    def log_into_mlflow(self):
        test = pd.read_csv(self.config.test_path)
        model = joblib.load(self.config.model_path)

        test_x = test.drop([self.config.target_column], axis =1)
        test_y = test[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_uri = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            predicted_qualities = model.predict(test_x)
            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

            scores = {
                "rmse": rmse,
                "mae": mae,
                "r2": r2
            }

            save_json(path = Path(self.config.metrics_path), data = scores)

            mlflow.log_params(self.config.all_params)
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)

            if tracking_uri != "file":
                mlflow.sklearn.log_model(model, "model" , registered_model_name="ElasticNetWineModel")
            else:
                mlflow.sklearn.log_model(model, "model")

            logger.info(f"Model logged into MLFlow")
            




