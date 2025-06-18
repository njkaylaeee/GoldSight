import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# --- Judul Halaman ---
st.title("📈 Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menampilkan beberapa model yang telah dilatih untuk memprediksi harga penutupan (*Close*) dari harga emas berdasarkan fitur:
- **Open**
- **High**
- **Low**
- **Volume**

Model dilatih dengan data historis dan dapat dibandingkan dari sisi karakteristik serta kompleksitasnya.
""")

# --- Pilihan Model ---
model_options = {
    "Linear Regression": "models/linear_regression_model.pkl",
    "Random Forest Regressor": "models/random_forest_model.pkl",
    "Gradient Boosting Regressor": "models/gradient_boosting_model.pkl"
}

selected_model_name = st.selectbox("Pilih Model untuk Ditampilkan:", list(model_options.keys()))
model_path = model_options[selected_model_name]

# --- Load Model ---
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model {selected_model_name} tidak ditemukan.")
    st.stop()

# --- Tampilkan Informasi Model ---
st.subheader(f"🧠 Informasi Model: {selected_model_name}")

if isinstance(model, LinearRegression):
    st.markdown("**Tipe:** Regresi Linear Sederhana")
    coef_df = pd.DataFrame({
        "Fitur": ["Open", "High", "Low", "Volume"],
        "Koefisien": model.coef_
    })
    st.dataframe(coef_df, use_container_width=True)
    st.write("**Intercept:**", model.intercept_)

elif isinstance(model, RandomForestRegressor) or isinstance(model, GradientBoostingRegressor):
    st.markdown("**Tipe:** Ensemble Tree-Based Regressor")
    importance_df = pd.DataFrame({
        "Fitur": ["Open", "High", "Low", "Volume"],
        "Feature Importance": model.feature_importances_
    }).sort_values(by="Feature Importance", ascending=False)
    st.bar_chart(importance_df.set_index("Fitur"))
else:
    st.warning("Tipe model tidak dikenali.")

# --- Penutup ---
st.info("Model ini akan digunakan pada halaman *Formulir Prediksi* untuk memprediksi harga emas berdasarkan input pengguna.")
