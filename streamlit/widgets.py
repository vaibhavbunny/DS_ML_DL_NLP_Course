import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name = st.text_input("Enter Your Name: ")
if name:
    st.write(f"My Name is {name}")

age = st.slider("Select your age: ",0,100,25)

options = ['Java','Python','C++','C']
st.write(f"Your age is {age}")

choice = st.selectbox("Choose Your Favourite Language: ", options)

st.write(f"Your Favourite Language is {choice}")

data = {
    "Name" : ['Vaibhav','Suhas','Kale','Diya','Mayur'],
    "Age" : [22,49,100,20,25],
    "City" : ['Bangalore','Karmala','Pimpalwadi','Kwd','Lonawla']
}

uploaded_file = st.file_uploader("Select a CSV File",type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)



