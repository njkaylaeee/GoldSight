import streamlit as st
import numpy as np
import pickle

st.title("📈 Formulir Prediksi Harga Emas")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.markdown("Masukkan data berikut untuk memprediksi harga penutupan emas:")

open_price = st.number_input("Open", min_value=0.0)
high_price = st.number_input("High", min_value=0.0)
low_price = st.number_input("Low", min_value=0.0)
volume = st.number_input("Volume", min_value=0.0)

if st.button("Prediksi"):
    input_data = np.array([[open_price, high_price, low_price, volume]])
    pred = model.predict(input_data)
    st.success(f"Prediksi Harga Penutupan: ${pred[0]:,.2f}")
