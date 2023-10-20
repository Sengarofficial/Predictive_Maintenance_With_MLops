from src.Mlflow_Project.config.configuration import ConfigurationManager
from src.Mlflow_Project.entity.config_entity import ModelTrainerConfig
from src.Mlflow_Project.components.model_trainer import ModelTrainer
from src.Mlflow_Project import logger 


STAGE_NAME = "Model Trainer Stage"

class ModelTrainerPipeline:
    def __init__(self):
        pass 



    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer_config = ModelTrainer(config = model_trainer_config)
        model_trainer_config.train()




if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
        obj = ModelTrainerPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<")
    except Exception as e:
        logger.exception(e)