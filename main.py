from src.ML_Project import logger # type: ignore
from src.ML_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline

STAGE_NAME = "DATA INGESTION"

if __name__ == "__main__":
    try:
        logger.info(f"Stagging Started {STAGE_NAME}")
        pipeline = DataIngestionPipeline
        pipeline.main()
        logger.info(f"Stagging Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Erro in the Stagging")
        raise e
    