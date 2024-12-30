from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_url : str
    local_data_files : Path
    unzip_dir : Path


@dataclass(frozen = True)
class DataValidationConfig:
    root_dir: Path
    unzip_dir: Path
    status_file: str
    all_schema: dict
    
@dataclass(frozen = True)
class DataTrasnformationConfig:
    root_dir : Path
    data_file : Path

@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir : Path
    train_path : Path
    test_path : Path
    model_name : str
    alpha : float
    l1_ratio : float
    target_column : str
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    model_path : Path
    test_path : Path
    metrics_path : Path
    all_params : dict
    target_column : str
    mlflow_uri : str