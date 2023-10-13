import pandas as pd 
import os
import joblib 
from src.Mlflow_Project.__init__ import logger 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from src.Mlflow_Project.constants import *
from src.Mlflow_Project.utils.utility import FileOperations
from src.Mlflow_Project.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    ## Note: You can add different data transformtion techniques such as Scaler, PCA and all 
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model 

    # defining train test split method 

    def train_test_split(self):
        data = pd.read_csv(self.config.data_path)

        # Split the data into training and test sets. (0.75, 0.25) split. 

        train, test = train_test_split(data)
        # Fit scaler on training data
        scaler = StandardScaler()
        X_train = scaler.fit_transform(train)
        logger.info("train scaling done..!!")

        
        X_test = scaler.transform(test)
        logger.info("test data transform done...!!")

        train_scaled_df = pd.DataFrame(X_train, columns= train.columns)
        test_scaled_df = pd.DataFrame(X_test, columns = test.columns)

        train_scaled_df.to_csv(os.path.join(self.config.root_dir, "train_scaled.csv"), index = False)
        test_scaled_df.to_csv(os.path.join(self.config.root_dir, "test_scaled.csv"), index = False)

        joblib.dump(scaler, os.path.join(self.config.root_dir, self.config.scaler_name))


        logger.info("Splitted data into train and test")
        logger.info(train.shape)
        logger.info(test.shape)


        print(train.shape)
        print(test.shape)

        