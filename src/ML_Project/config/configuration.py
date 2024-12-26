from ML_Project.constants import *
from ML_Project.utils.common import read_yaml, create_directories
from ML_Project.entity.config_entity  import DataIngestionConfig
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
    
    

                 
    
        