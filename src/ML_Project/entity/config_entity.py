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