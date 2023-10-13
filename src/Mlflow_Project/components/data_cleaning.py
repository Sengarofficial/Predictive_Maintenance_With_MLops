import os 
from src.Mlflow_Project.__init__ import logger 
from src.Mlflow_Project.entity.config_entity import DataCleaningConfig
import pandas as pd 
import numpy as np 


class DataCleaning:
    def __init__(self, config: DataCleaningConfig):
        self.config = config


    ## Note: You can add different data transformtion techniques such as Scaler, PCA and all 
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model 

    # defining train test split method 

    def data_cleaning(self):
        df = pd.read_csv(self.config.unzip_data_dir_train, sep = " ")

        columns_to_drop = ['Unnamed: 26', 'Unnamed: 27']
        df = df.drop(columns=columns_to_drop)

        index_names = ['engine', 'cycle']
        setting_names = ['setting_1', 'setting_2', 'setting_3']
        sensor_names= [ "(Fan inlet temperature) (◦R)",
                "(LPC outlet temperature) (◦R)",
                "(HPC outlet temperature) (◦R)",
                "(LPT outlet temperature) (◦R)",
                "(Fan inlet Pressure) (psia)",
                "(bypass-duct pressure) (psia)",
                "(HPC outlet pressure) (psia)",
                "(Physical fan speed) (rpm)",
                "(Physical core speed) (rpm)",
                "(Engine pressure ratio(P50/P2)",
                "(HPC outlet Static pressure) (psia)",
                "(Ratio of fuel flow to Ps30) (pps/psia)",
                "(Corrected fan speed) (rpm)",
                "(Corrected core speed) (rpm)",
                "(Bypass Ratio) ",
                "(Burner fuel-air ratio)",
                "(Bleed Enthalpy)",
                "(Required fan speed)",
                "(Required fan conversion speed)",
                "(High-pressure turbines Cool air flow)",
                "(Low-pressure turbines Cool air flow)" ]

        col_names = index_names + setting_names + sensor_names
        df.columns = col_names


        print("na values available in data \n")
        print(df.isna().sum())
        df = df.dropna()
        print("after droping na values \n")
        print(df.isna().sum())
        print("Uniques Values : ")
        print(df.nunique())
        print("Observing columns with only one uniques values: ")
        unwanted=[]
        for i in df.select_dtypes(include= np.number):
            if df[i].nunique()==1:
                unwanted.append(i)
        print(unwanted)
        print("columns have only one unique value, so we are dropping theses columns")
        df.drop(columns=unwanted, inplace=True)

        drop_columns = ['(Corrected core speed) (rpm)']

        df.drop(columns = drop_columns, axis=1, inplace=True)

        # add target fucntion 
        # define the maximum life of each engine, 
        #as this could be used to obtain the RUL at each point in time of the engine's life 

        #remaining useful life (RUL) of each engine in the test dataset.
        #RUL is equivalent of number of flights remained for the engine after the last datapoint in the test dataset.

        data_rul = df.groupby(['engine']).agg({'cycle':'max'})
        data_rul.rename(columns={'cycle':'life'},inplace=True)

        data_train = df.merge(data_rul,how='left',on=['engine'])

        data_train['RUL']=data_train['life']-data_train['cycle']
        data_train.drop(['life'],axis=1,inplace=True)

        drop_columns = ['(Corrected fan speed) (rpm)','(Physical fan speed) (rpm)','(HPC outlet temperature) (◦R)']
        data_train.drop(columns = drop_columns, axis=1, inplace=True)
        
        data_train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index = False)
        #test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index = False)

    
