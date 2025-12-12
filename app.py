import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(page_title="AutoML Income Predictor", layout="wide")

st.title("💼 Income Prediction – AutoML Best Model")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("best_model.pkl")

model = load_model()

st.success("Model loaded successfully!")

# User Input Form
st.subheader("Enter details to predict income")

age = st.number_input("Age", 18, 90, 30)
education_num = st.number_input("Education Number", 1, 16, 10)
capital_gain = st.number_input("Capital Gain", 0, 100000, 0)
capital_loss = st.number_input("Capital Loss", 0, 50000, 0)
hours_per_week = st.number_input("Hours per week", 1, 100, 40)
fnlwgt = st.number_input("Final Weight (fnlwgt)", 10000, 2000000, 100000)

data = pd.DataFrame({
    "age": [age],
    "fnlwgt": [fnlwgt],
    "education-num": [education_num],
    "capital-gain": [capital_gain],
    "capital-loss": [capital_loss],
    "hours-per-week": [hours_per_week]
})

if st.button("Predict Income"):
    prediction = model.predict(data)[0]
    income = ">50K" if prediction == 1 else "<=50K"
    st.subheader(f"Predicted Income: **{income}**")
