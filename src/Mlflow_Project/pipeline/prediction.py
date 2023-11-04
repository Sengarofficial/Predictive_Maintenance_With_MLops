import joblib 
import numpy as np 
import pandas as pd 
from pathlib import Path 
from typing import Any
from src.Mlflow_Project.utils.utility import FileOperations


class ScalingPipeline:
    def __init__(self):
        self.scaler = joblib.load(Path("artifacts/data_transformation/scaler.joblib"))
        

    def scale(self, data):
        scaling = self.scaler.transform(data)

        return scaling

class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path("artifacts/model_trainer/model.joblib"))
        pass 



    def predict(self, data):
        prediction = self.model.predict(data)


        return prediction 
    
    