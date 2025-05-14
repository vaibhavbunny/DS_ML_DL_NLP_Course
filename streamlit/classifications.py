import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

# Load data
df, target_name = load_data()

# Train model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])  # Use all columns except 'species' for training

# Sidebar inputs for features
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length (cm)", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal Width (cm)", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()))
petal_length = st.sidebar.slider("Petal Length (cm)", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()))
petal_width = st.sidebar.slider("Petal Width (cm)", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()))

# Prepare input data for prediction
input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_name[prediction[0]]

# Display the prediction result
st.write(f"The predicted species is: **{predicted_species}**")


