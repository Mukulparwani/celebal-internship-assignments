# app.py
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("iris_model.pkl")

# Title
st.title("🌸 Iris Flower Classifier")
st.markdown("Enter flower measurements to predict the species")

# Input sliders
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Predict button
if st.button("Predict"):
    inputs = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(inputs)[0]
    classes = ['Setosa', 'Versicolor', 'Virginica']
    st.success(f"🌼 Predicted Species: {classes[prediction]}")
