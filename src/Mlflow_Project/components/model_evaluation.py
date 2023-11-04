# component 


import os 
import json
from pathlib import Path
import pandas as pd 
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow 
import mlflow.sklearn 
import numpy as np 
import joblib 
from src.Mlflow_Project.entity.config_entity import ModelEvaluationConfig
from src.Mlflow_Project.constants import *
from src.Mlflow_Project.utils.utility import FileOperations








class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config 


    def eval_metrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2 
    
    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        test_data.dropna(subset=[self.config.target_column], inplace=True)
        test_y = pd.read_csv(self.config.test_y)
        #test_y = pd.read_csv(self.config.test_y).values
        #print(test_y)


        model = joblib.load(self.config.model_path)


        test_x = test_data.drop([self.config.target_column], axis = 1)
        #test_y = test_data[[self.config.target_column]]

        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():

            predicted_qualities = model.predict(test_x)
            print(predicted_qualities)

            (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)


            # Saving metrics as local 
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            FileOperations.save_json(path = Path(self.config.metric_file_name), data = scores)


            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            # Model registry does not work with file store 
            if tracking_url_type_store == "file":


                # Register the model 
                # There are other ways to use the model registry, which depends on the use case,
                # please refer to the doc for more information:
                # http://mlflow.org/docs/latest/model-registry-.html#api-workflow
                mlflow.sklearn.log_model(model, 'model', registered_model_name= "ElasticnetModel")
            else:
                mlflow.sklearn.log_model(model, "model")
                

            
                

            