import streamlit as st 
import numpy as np
import pandas as pd

## Title of the Application
st.title("Hello Streamlit")
## Display a Simple Text
st.write("This is a Simple Text")

## Create a DataFrame

df = pd.DataFrame({
    'First Column' : [1,2,3,4],
    'Second Column' : [10,20,30,40]
})


## Display the dataframe
st.write("Display the dataframe")
st.write(df)

## Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)