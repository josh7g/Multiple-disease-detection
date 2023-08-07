#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 13:55:16 2023

@author: joshuanketsiah
"""

import numpy as np
import pickle
import streamlit as st

#loading the model
loaded_model = pickle.load(open("/Users/joshuanketsiah/Desktop/trained_model.sav","rb"))

#creating a fuunction for prediction
def diabetes_prediction(input_data):

   # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'This person is not Diabetic'
    else:
      return 'This person is Diabetic'

def main():
    #giving a title
    st.title("Diabetes Prediction Application")
    
    #getting input from the user
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose Level")
    BloodPressure = st.text_input("Blood Pressure Value")
    SkinThickness = st.text_input("Skin Thickness Value")
    Insulin = st.text_input("Insulin Value")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age")
    
    #code for prediction
    diagnosis = ""
    
    #creating a button for prediction
    if st.button("Test Result"):
                 diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
                 
    st.success(diagnosis)
                 
if __name__ == "__main__":
    main()

    
    
    
    
    
    
    
    
    