from ML_Project import logger
from ML_Project.config.configuration import ModelEvaluationConfig, ConfigurationManager
from ML_Project.utils.common import read_yaml, create_directories, save_json
from pathlib import Path
import joblib
from ML_Project.components.model_evaluation import ModelEvaluation

STAGE_NAME = "MODEL EVALUATION"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            model_eval_config = config_manager.get_model_eval_config()
            model_evaluation = ModelEvaluation(config=model_eval_config)
            model_evaluation.log_into_mlflow()

        except Exception as e:
            logger.error(e)
            raise e


if __name__ == "__main__":
    try:
        logger.info(f"Evaluation Started {STAGE_NAME}")
        pipeline = ModelEvaluationPipeline()
        pipeline.main()
        logger.info(f"Evaluation Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Evaluation Error")
        raise e