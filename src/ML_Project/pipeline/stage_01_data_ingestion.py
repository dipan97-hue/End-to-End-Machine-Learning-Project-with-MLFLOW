from ML_Project.config.configuration import ConfigurationManager
from ML_Project.components.data_ingestion import DataIngestion
from ML_Project import logger

STAGE_NAME = "DATA INGESTION"

class DataIngestionPipeline:
    def __init__(self):
        pass
    @staticmethod
    def main():
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.unzip_data()

if __name__ == "__main__":
    try:
        logger.info(f"Stagging Started {STAGE_NAME}")
        pipeline = DataIngestionPipeline()
        pipeline.main()
        logger.info(f"Stagging Completed {STAGE_NAME}")

    except Exception as e: 
        logger.info("Erro in the Stagging")
        raise e
    
