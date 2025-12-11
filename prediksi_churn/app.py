import streamlit as st
import numpy as np
import pandas as pd
from model_prediksi import predict_churn

st.set_page_config(page_title="Churn Prediction App", page_icon="📊", layout="wide")

st.title("📊 Prediksi Risiko Churn Pelanggan Bank")
st.write("Masukkan data pelanggan untuk memprediksi risiko churn.")

# ======================
# INPUT FORM
# ======================
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=650)
country = st.selectbox("Country", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=35)
tenure = st.number_input("Tenure (Years)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=10000.0, format="%.2f")
products_number = st.number_input("Product Numbers", min_value=1, max_value=4, value=2)
credit_card = st.selectbox("Credit Card", [0, 1])
active_member = st.selectbox("Active Member", [0, 1])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=50000.0, format="%.2f")

# ======================
# PREDICT BUTTON
# ======================
if st.button("Prediksi Churn"):
    
    data = {
        "credit_score": [credit_score],
        "country": [country],
        "gender": [gender],
        "age": [age],
        "tenure": [tenure],
        "balance": [balance],
        "products_number": [products_number],
        "credit_card": [credit_card],
        "active_member": [active_member],
        "estimated_salary": [estimated_salary]
    }

   
    pred, prob = predict_churn(data)

    st.subheader("📌 Hasil Prediksi:")
    if pred == 1:
        st.error(f"⚠ Pelanggan berisiko churn! (Probabilitas: {prob:.2f})")
    else:
        st.success(f"✅ Pelanggan tidak berisiko churn. (Probabilitas: {prob:.2f})")
    