import os
from ML_Project import logger
from ML_Project.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
    def validate_all(self)->bool:
        
        try:
            validation_status = None
            data = pd.read_csv(self.config.unzip_dir)
            all_cols = list(data.columns)
            
            # print(all_cols)
            all_schema = self.config.all_schema.COLUMNS.keys()
            print(all_schema)
            if len(all_cols) != len(all_schema):
                all_cols = all_cols[:-1]
            print(all_cols)
            
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation status:{validation_status}')
                else:
                    validation_status = True
                    with open(self.config.status_file, 'w') as f:
                        f.write(f'Validation status:{validation_status}')
            return validation_status
        except Exception as e:
            raise e
        
        