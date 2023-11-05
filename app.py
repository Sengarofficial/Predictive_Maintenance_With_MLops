from flask import Flask, render_template, request 
import os 
import numpy as np 
import pandas as pd 
from src.Mlflow_Project.pipeline.prediction import ScalingPipeline, PredictionPipeline


app = Flask(__name__)   # initializing my flask app 

@app.route('/', methods = ['GET'])  # route to display the home page 
def homePage():
    return render_template("index.html")


@app.route('/train', methods = ['GET']) # route to train the pipeline 
def training():
    os.system("python main.py")
    return "Training Succesful"

@app.route('/predict', methods = ['POST', 'GET']) # route to show the predictions in oour web ui 
def index():
    if request.method == 'POST':
        try:
            # reading the inputs given by the user 
            engine = int(request.form['engine'])
            cycle = int(request.form['cycle'])
            setting_1 = float(request.form['setting_1'])
            setting_2 = float(request.form['setting_2'])
            LPC_outlet_temperature_degR = float(request.form['LPC_outlet_temperature_degR'])
            LPT_outlet_temperature_degR = float(request.form['LPT_outlet_temperature_degR'])
            bypass_duct_pressure_psia = float(request.form['bypass_duct_pressure_psia']) 
            HPC_outlet_pressure_psia = float(request.form['HPC_outlet_pressure_psia']) 
            Physical_core_speed_rpm = float(request.form['Physical_core_speed_rpm'])  
            HPC_outlet_Static_pressure_psia = float(request.form['HPC_outlet_Static_pressure_psia']) 
            Ratio_of_fuel_flow_to_Ps30_pps_psia = float(request.form['Ratio_of_fuel_flow_to_Ps30_pps_psia'])
            Bypass_Ratio = float(request.form['Bypass_Ratio'])
            Bleed_Enthalpy = int(request.form['Bleed_Enthalpy'])
            High_pressure_turbines_Cool_air_flow = float(request.form['High_pressure_turbines_Cool_air_flow'])
            Low_pressure_turbines_Cool_air_flow = float(request.form['Low_pressure_turbines_Cool_air_flow'])
            
            # converting all input data to list then list to numpy array 
            data = [engine, cycle, setting_1, setting_2, LPC_outlet_temperature_degR, LPT_outlet_temperature_degR, bypass_duct_pressure_psia, HPC_outlet_pressure_psia, Physical_core_speed_rpm, HPC_outlet_Static_pressure_psia, Ratio_of_fuel_flow_to_Ps30_pps_psia, Bypass_Ratio, Bleed_Enthalpy, High_pressure_turbines_Cool_air_flow, Low_pressure_turbines_Cool_air_flow]   
            data = np.array(data).reshape(1, 15)

            scl = ScalingPipeline()
            data_scaled = scl.scale(data)

            obj = PredictionPipeline()
            predict = obj.predict(data_scaled)  

            return render_template('results.html', prediction = str(predict))
        except Exception as e:
            return str(e)

    else:
        return render_template('index.html')
                                      
                                      
                                      

if __name__ == '__main__':
    #app.run(host = "0.0.0.0", port = 6060, debug = True)
    app.run(host = "0.0.0.0", port = 6060)

