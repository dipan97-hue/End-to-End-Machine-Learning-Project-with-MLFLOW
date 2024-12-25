import os
from box.exceptions import BoxValueError
from ML_Project import logger
import yaml
import joblib
import json
from box import ConfigBox
from ensure import ensure_annotations
from pathlib import Path
from typing import Any, Dict, List, Tuple

@ensure_annotations
def read_yaml(path_to_yaml: Path) ->ConfigBox:
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"Yaml file loadded successfully from {path_to_yaml}")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories : list):
    for path in path_to_directories:
        os.makedirs(path, exist_ok = True)
    logger.info(f"Directory created at {path}")

@ensure_annotations
def save_json(path : Path, data : Dict):
    try:
        with open(path, "w") as json_file:
            json.dump(data, json_file, indent = 4)
        logger.info(f"Data saved at {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def load_json(path : Path) -> ConfigBox:
    try:
        with open(path, 'r') as f:
            content = json.load(f)
        logger.info(f"Data loaded from {path}")
        return ConfigBox(content)
    except  Exception as e:
        raise e
    
@ensure_annotations
def save_bin(path: Path, data: Any):
    try:
        joblib.dump(data, path)
        logger.info(f"Data saved at {path}")
    except Exception as e:
        raise e
    
@ensure_annotations
def load_bin(path: Path)-> Any:
    try:
        data = joblib.load(path)
        logger.info(f"Data Loaded from {path}")
        return data
    except Exception as e:
        raise e
    
@ensure_annotations
def get_size(path: Path) -> str:

    size = round(os.path.getsize(path)/1024)
    return f"{size} KB"




