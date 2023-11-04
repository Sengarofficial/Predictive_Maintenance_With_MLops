from src.Mlflow_Project.constants import *
from src.Mlflow_Project.utils.utility import FileOperations
from src.Mlflow_Project.entity.config_entity import (DataIngestionConfig, DataCleaningConfig,
                                                     DataValidationConfig, DataTransformationConfig, 
                                                     ModelTrainerConfig, ModelEvaluationConfig)
import os
from dotenv import load_dotenv
load_dotenv()
MLFLOW_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")

# configuration manager class , will read all yaml files 

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = FileOperations.read_yaml(config_filepath)
        self.params = FileOperations.read_yaml(params_filepath)
        self.schema = FileOperations.read_yaml(schema_filepath)

        FileOperations.create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        FileOperations.create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config
    


    def data_cleaning_config(self) -> DataCleaningConfig:
        config = self.config.data_cleaning

        FileOperations.create_directories([config.root_dir])

        data_cleaning_config = DataCleaningConfig(
            root_dir=config.root_dir,
            unzip_data_dir_train = config.unzip_data_dir_train

        )

        return data_cleaning_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS


        FileOperations.create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir = config.root_dir,
            STATUS_FILE = config.STATUS_FILE,
            clean_data_dir = config.clean_data_dir,
            all_schema=schema,
        
    )


        return data_validation_config 
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
            
            config = self.config.data_transformation

            FileOperations.create_directories([config.root_dir])

            data_transformation_config = DataTransformationConfig(
                 root_dir = config.root_dir,
                 data_path = config.data_path,
                 scaler_name = config.scaler_name,

            )
            
            return data_transformation_config
    


    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.ElasticNet
        schema = self.schema.TARGET_COLUMN


        FileOperations.create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir=config.root_dir,
            train_data_path = config.train_data_path,
            test_data_path = config.test_data_path,
            model_name = config.model_name,
            imputer_name= config.imputer_name,
            alpha = params.alpha,
            l1_ratio = params.l1_ratio,
            target_column = schema.name

        )

        return model_trainer_config
    

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
            config = self.config.model_evaluation
            params = self.params.ElasticNet
            schema = self.schema.TARGET_COLUMN


            FileOperations.create_directories([config.root_dir])


            model_evaluation_config = ModelEvaluationConfig(
                 root_dir = config.root_dir,
                 test_data_path= config.test_data_path,
                 model_path = config.model_path,
                 all_params = params,
                 metric_file_name = config.metric_file_name,
                 target_column= schema.name,
                 mlflow_uri= MLFLOW_URI,
            )

            return model_evaluation_config
    


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
                config = self.config.model_evaluation
                params = self.params.ElasticNet
                schema = self.schema.TARGET_COLUMN


                FileOperations.create_directories([config.root_dir])


                model_evaluation_config = ModelEvaluationConfig(
                    root_dir = config.root_dir,
                    test_data_path= config.test_data_path,
                    test_y = config.test_y,
                    model_path = config.model_path,
                    all_params = params,
                    metric_file_name = config.metric_file_name,
                    target_column= schema.name,
                    mlflow_uri= MLFLOW_URI,
                )

                return model_evaluation_config