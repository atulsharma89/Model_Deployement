#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 16:40:22 2020

@author: atul595525
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

#Swagger will be an API thing and will generated the front end UI part



#app=Flask(__name__)

#load our classifier.pkl file

app = Flask(__name__, template_folder='templates')
Swagger(app)
with open('/Users/atul595525/Desktop/learning/Edureka_courses/Docker_ML_Flask_App/classifier_1.pkl', 'rb') as model_pkl:
    rf = pickle.load(model_pkl)




#pickel_in=open('/Users/atul595525/Desktop/learning/Edureka_courses/Docker_ML_Flask_App/classifier_1.pkl','rb')
#classifier=pickle.load(pickel_in)


#Step 3: create function to show something at http://127.0.0.1:5000/
#create decorator to make this work in flask

@app.route('/')
def welcome():
    return "Welcome All"
    

#Step 4: create another function to provide parmeteres to my model to predict the output value

# Create an API endpoint
@app.route('/predict')
def predict_new():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    # Read all necessary request parameters 
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    # prediction for new data
    new = np.array([[variance, skewness, curtosis, entropy]])
    result = rf.predict(new)
    
    # return the result back
    return 'Prediction for the given input: {} is: {}'.format(new, result)


'''
@app.route('/predict',methods=['GET'])
def predict_note_authentication():    
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    new = np.array([[variance,skewness,curtosis,entropy]])
    #prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    prediction=classifier.predict(new)
    #return "The predicted value is" + str(prediction)
    return 'Prediction for the given input: {} is: {}'.format(new, prediction)
    #print(prediction)
'''

#@app.route is a decorator in Python
#https://medium.com/@nguyenkims/python-decorator-and-flask-3954dd186cda
#a decorator is a function that takes another function and extends the behavior of the latter function without explicitly modifying it
#By having app.route as decorator, the function index is registered for the route / so that when that route is requested, index is called and its result “Hello world” is returned back to the client (be it a web browser, curl, etc).


@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    prediction=rf.predict(df_test)
    return "The predicted value for the file is" + str(list(prediction))
    #print(prediction)

#http://127.0.0.1:5000/
#http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1
#http://127.0.0.1:5000/predict?variance=0.0006&skewness=20&curtosis=2&entropy=0

if __name__=='__main__':
    app.run()
    