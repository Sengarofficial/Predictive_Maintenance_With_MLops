from flask import Flask, render_template, request 
import os 
import numpy as np 
import pandas as pd 
from src.Mlflow_Project.pipeline.prediction import PredictionPipeline


app = Flask(__name__)   # initializing my flask app 

@app.route('/', methods = ['GET'])  # route to display the home page 
def homePage():
    return render_template("index.html")


@app.route('/train', methods = ['GET']) # route to train the pipeline 
def training():
    os.system("python main.py")
    return "Training Succesful"


if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 6060, debug = True)

