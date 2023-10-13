# update the pipeline 

from src.Mlflow_Project.config.configuration import ConfigurationManager
from src.Mlflow_Project.components.data_transformation import DataTransformation
from src.Mlflow_Project import logger 

STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass 


    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)  
        data_transformation.train_test_split()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)