# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:05:38 2023

@author: vinay
"""

from flask import Flask, request
import pickle
import numpy as np
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

#http://localhost:5000/Model_Prediction

model_pk = pickle.load(open('Ev_Price_Pred.pkl' , 'rb'))

@app.route('/Model_Prediction' , methods=["GET", "POST"])
def Model_Prediction():
    if request.method == "GET":
        return 'Please send post request'
    elif request.method == "POST":
        data = request.get_json()
        
        AccelSec = data["AccelSec"]
        TopSpeed_KmH = data["TopSpeed_KmH"]
        Range_Km = data["Range_Km"]
        Efficiency_WhKm = data["Efficiency_WhKm"]
        Seats = data["Seats"]
        
        in1 = np.array([[AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,Seats]])
        prediction = model_pk.predict(in1)
        return str(prediction)
    
app.run()   
