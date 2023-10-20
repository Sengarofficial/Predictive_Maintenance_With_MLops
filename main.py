from src.Mlflow_Project import logger 
from src.Mlflow_Project.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.Mlflow_Project.pipeline.stage_02_data_cleaning import DataCleaningPipeline
from src.Mlflow_Project.pipeline.stage_03_data_validation import DataValidationPipeline
from src.Mlflow_Project.pipeline.stage_04_data_transformation import DataTransformationPipeline
from src.Mlflow_Project.pipeline.stage_05_model_trainer import ModelTrainerPipeline
from src.Mlflow_Project.pipeline.stage_06_model_evaluation import ModelEvaluationPipeline


STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)



STAGE_NAME = "Data Cleaning Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataCleaningPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Validation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Data Transformation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Trainer Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelTrainerPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
except Exception as e:
    logger.exception(e)