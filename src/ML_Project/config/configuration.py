from ML_Project.constants import *
from ML_Project.utils.common import read_yaml, create_directories
from ML_Project.entity.config_entity  import DataIngestionConfig, DataValidationConfig, DataTrasnformationConfig
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
    

                 
    
        