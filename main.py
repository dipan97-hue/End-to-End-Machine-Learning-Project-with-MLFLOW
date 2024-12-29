from src.ML_Project import logger # type: ignore
from src.ML_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.ML_Project.pipeline.stage_02_data_validation import DataValidationPipeline

STAGE_NAME = "DATA INGESTION"
try:
    logger.info(f"Stagging Started {STAGE_NAME}")
    pipeline = DataIngestionPipeline
    pipeline.main()
    logger.info(f"Stagging Completed {STAGE_NAME}")

except Exception as e: 
    logger.info("Erro in the Stagging")
    raise e

STAGE_NAME = "DATA VALIDATION"   
try:
    logger.info(f"Stagging Started {STAGE_NAME}")
    pipeline = DataValidationPipeline()
    pipeline.main()
    logger.info(f"Stagging Completed {STAGE_NAME}")

except Exception as e: 
    logger.info("Error in the Stagging")
    raise e