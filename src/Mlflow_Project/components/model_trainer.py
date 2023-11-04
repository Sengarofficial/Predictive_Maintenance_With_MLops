# defining component

import pandas as pd
import os 
from src.Mlflow_Project.__init__ import logger 
from sklearn.linear_model import ElasticNet
from sklearn.impute import SimpleImputer
from src.Mlflow_Project.entity.config_entity import ModelTrainerConfig
import joblib 





        # components 

class ModelTrainer:
    def __init__(self, config):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Drop rows with missing values in the target column
        train_data.dropna(subset=[self.config.target_column], inplace=True)
        test_data.dropna(subset=[self.config.target_column], inplace=True)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]

        # Create an imputer to fill missing values with a specific strategy (e.g., mean or median)
        imputer = SimpleImputer(strategy='mean')

        # Fit the imputer on the training data and transform the test data
        train_y_impute = imputer.fit_transform(train_y)
        test_y = imputer.transform(test_data[[self.config.target_column]].values.reshape(-1, 1))

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y_impute)

        test_x = pd.DataFrame(test_x, columns=test_x.columns)
        test_y = pd.DataFrame(test_y, columns=[self.config.target_column])

        # Save the scaled datasets and target variables
        test_x.to_csv(os.path.join(self.config.root_dir, "test_x.csv"), index=False)
        test_y.to_csv(os.path.join(self.config.root_dir, "test_y.csv"), index=False)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
        joblib.dump(imputer, os.path.join(self.config.root_dir, self.config.imputer_name))

        