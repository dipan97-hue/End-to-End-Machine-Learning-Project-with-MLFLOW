from ML_Project.constants import *
from ML_Project.utils.common import read_yaml, create_directories
from ML_Project.entity.config_entity  import ( 
    DataIngestionConfig, DataValidationConfig, DataTrasnformationConfig , ModelTrainerConfig, ModelEvaluationConfig)
class ConfigurationManager:
    def __init__(self,
                 config_path = Config_File_Path,
                 params_path = Params_File_Path,
                 schema_path = Schema_File_Path):
        self.config = read_yaml(config_path)
        self.params = read_yaml(params_path)
        self.schema = read_yaml(schema_path)
        create_directories([self.config['artifacts_root']])
   

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir,
            source_url = config.source_url,
            local_data_files = config.local_data_files,
            unzip_dir= config.unzip_dir
        )

        return data_ingestion_config
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            status_file = config.status_file,
            all_schema = self.schema,
            unzip_dir= config.unzip_data_dir
        )

        return data_validation_config
    def get_data_transformation_config(self) -> DataTrasnformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTrasnformationConfig(
            root_dir = config.root_dir,
            data_file = config.data_path
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir = config.root_dir,
            train_path = config.train_path,
            test_path = config.test_path,
            model_name = config.model_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name
        )

        return model_trainer_config
    
    def get_model_eval_config(self) -> ModelEvaluationConfig:
        config = self.config.model_evaluation
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_evaluation_config = ModelEvaluationConfig(
            root_dir = config.root_dir,
            model_path = config.model_path,
            test_path = config.test_path,
            metrics_path = config.metrics_path,
            all_params = params,
            target_column = schema.name,
            mlflow_uri = 'https://dagshub.com/dipan97-hue/End-to-End-Machine-Learning-Project-with-MLFLOW.mlflow'
            
        )
        return model_evaluation_config             
    
        