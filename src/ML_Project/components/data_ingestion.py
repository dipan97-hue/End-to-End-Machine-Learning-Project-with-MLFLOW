import os
import zipfile
import requests
from ML_Project import logger
from ML_Project.utils.common import get_size
from pathlib import Path
from ML_Project.entity.config_entity  import DataIngestionConfig

class DataIngestion:
    def __init__(self, config):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_files):
            response = requests.get(self.config.source_url)
            response.raise_for_status()
            with open(self.config.local_data_files, 'wb') as f:
                f.write(response.content)
            logger.info(f"Downloading file ")
        else:
            logger.info(f"Data already exists with size {get_size(self.config.local_data_files)}")

    def unzip_data(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_files, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

    
