from flask import Flask,render_template,request
import joblib
import pandas as pd 
import os


app = Flask(__name__)


model = joblib.load('model/svm_last.joblib')

data = pd.read_csv('forweb.csv')
df = []
for i in data.index:
    df.append([data['data'][i],data['label'][i]])



from app.routes import *

