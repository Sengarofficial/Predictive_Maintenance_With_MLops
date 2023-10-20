# update the pipeline 

from src.Mlflow_Project.config.configuration import ConfigurationManager
from src.Mlflow_Project.components.data_cleaning import DataCleaning
from src.Mlflow_Project import logger 


STAGE_NAME = "Data Cleaning Stage"

class DataCleaningPipeline:
    def __init__(self):
        pass 


    def main(self):
        config = ConfigurationManager()
        data_cleaning_config = config.data_cleaning_config()
        data_cleaning = DataCleaning(config = data_cleaning_config)  
        data_cleaning.data_cleaning()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataCleaningPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)