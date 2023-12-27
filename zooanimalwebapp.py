# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:15:54 2023

@author: nikitha
"""

import numpy as np
import pickle 
import streamlit as st



loaded_model=pickle.load(open("C:/Users/nikitha/Downloads/zoo_animal_webapp/zoo_animal_class_model.sav",'rb'))

#creating a function for classification
def zoo_animal_classification(input_data):
    
    input_data_as_array=np.asarray(input_data)
    
    input_data_reshaped=input_data_as_array.reshape(1,-1)
    
    prediction=loaded_model.predict(input_data_reshaped)
    
    if prediction[0]==1:
        return 'The animal is classified as Mammal'
    elif prediction[0]==2:
        return "The animal is classified as Bird"
    elif prediction[0]==3:
        return 'The animal is classified as RTeptile'
    elif prediction[0]==4:
        return "The animal is classified as Fish"
    elif prediction[0]==5:
        return 'The animal is classified as Amphibian'
    elif prediction[0]==6:
        return "The animal is classified as Bug"
    elif prediction[0]==7:
        return 'The animal is classified as Invertebrate'
        
def main():
    #giving a title
    st.title('Zoo Animal Classification Web App')
   
    #getting the input from user
    Hair=st.text_input('Enter 1 if hair is present, 0 for not')
    
    Feathers=st.text_input('Enter 1 if feathers is present, 0 for not')
    
    Eggs=st.text_input('Enter 1 if it lays eggs, 0 for not')
    
    Milk=st.text_input('Enter 1 if it produce milk, 0 for not')
    
    Airborne=st.text_input('Enter 1 if it is airborne, 0 for not')
    
    Aquatic=st.text_input('Enter 1 if it is aquatic, 0 for not')
    
    Predator=st.text_input('Enter 1 if it is a predator, 0 if it is a prey')
    
    Toothed=st.text_input('Enter 1 if its toothed, 0 for not')
    
    Backbone=st.text_input('Enter 1 if it has backbone, 0 for not')
    
    Breathes=st.text_input('Enter 1 if it breathes on land, 0 if under water')
    
    Venomous=st.text_input('Enter 1 if it is venomous, 0 for not')
    
    Fins=st.text_input('Enter 1 if it has fins , 0 for not')
    
    Legs=st.text_input('Enter the number of legs the mammal has 0/2/4/5/6/8')
    
    Tail=st.text_input('Enter 1 if it has tail, 0 for not')
    
    Domestic=st.text_input('Enter 1 if it is domestic animal, 0 for not')
    
    Catsize=st.text_input('Enter 0 if the mammal has similar size as that of a cat, 1 for not')
    
    #code for prediction 
    classification=''
    
    #creating a button for prediction
    if st.button('Animal Classification Result'):
        classification=zoo_animal_classification([Hair,Feathers,Eggs,Milk,Airborne,Aquatic,Predator,Toothed,Backbone,Breathes,Venomous,Fins,Legs,Tail,Domestic,Catsize])
        
    st.success(classification)
    
if __name__ =='__main__':
    main()
    