import numpy as np
import pickle
import pandas as pd
import streamlit as st 
from sklearn import datasets
from PIL import Image


pickle_in = open("model.pk","rb")
model = pickle.load(pickle_in)
df = pd.read_csv('gender_classification_v7.csv')

def welcome():
    return "Welcome All"

def predict(long_hair, forehead_width,forehead_height,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long):
    new_data = [[long_hair, forehead_width,forehead_height,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long]]
    pred = model.predict(new_data)
    return pred

def main():
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Gender Detection </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    #Hair
    long_hair = st.radio("Pilih Hair",('Long','Short'))
    if long_hair == "Long":
        long_hair = 1
    else:
        long_hair = 0
        
    #Forehead Widht
    forehead_width = st.slider('Lebar Dahi', min_value = float(df['forehead_width_cm'].min()), max_value = float((df['forehead_width_cm'].max())),step = 0.1)
    
    #Forehead Height
    forehead_height = st.slider('Tinggi Dahi',min_value = float(df['forehead_height_cm'].min()), max_value = float((df['forehead_height_cm'].max())),step= 0.1)
    
    #Lebar Hidung
    nose_wide = st.radio("Apakah Hidungnya Lebar?",("Yes","No"))
    if nose_wide == "Yes":
      nose_wide = 1
    else : 
      nose_wide= 0
    
    #Panjang Hidung
    nose_long = st.radio("Apakah Hidungnya Panjang?",("Yes","No"))
    if nose_long == "Yes":
      nose_long = 1
    else : 
      nose_long= 0

    #Tebal Bibir
    lips_thin = st.radio("Apakah Bibirnya tipis?",("Yes","No"))
    if lips_thin == "Yes":
      lips_thin = 1
    else : 
      lips_thin= 0
#           py -m streamlit run UAS.py
    # Panjang Hidung Ke Mulut
    distance_nose_to_lip_long = st.radio("Apakah Jarak Antara Hidung dan Mulut Panjang?",("Yes","No"))
    if distance_nose_to_lip_long == "Yes":
      distance_nose_to_lip_long = 1
    else : 
      distance_nose_to_lip_long= 0

    result=""
    if st.button("Predict"):
        result=predict(long_hair,forehead_width,forehead_height,nose_wide,nose_long,lips_thin,distance_nose_to_lip_long)
    st.success('The output is {}'.format(result))
if __name__=='__main__':
    main()