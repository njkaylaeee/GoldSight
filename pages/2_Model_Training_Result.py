import streamlit as st
import pandas as pd
import pickle
import os
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

# --- Judul Halaman ---
st.title("Model Prediksi Harga Emas")

st.markdown("""
Pada halaman ini, Anda dapat meninjau model-model machine learning yang telah dilatih untuk memprediksi harga **penutupan emas** berdasarkan fitur historis seperti:

- Open
- High
- Low
- Volume

Tiga model regresi yang digunakan:
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
""")

# --- Pilihan Model ---
model_dict = {
    "Linear Regression": "models/linear_regression_model.pkl",
    "Random Forest Regressor": "models/random_forest_model.pkl",
    "Gradient Boosting Regressor": "models/gradient_boosting_model.pkl"
}

selected_model = st.selectbox("Pilih Model:", list(model_dict.keys()))
model_path = model_dict[selected_model]

# --- Load Model ---
try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error(f"Model '{selected_model}' tidak ditemukan di path: {model_path}")
    st.stop()

st.subheader(f"Detail Model: {selected_model}")

# --- Tampilkan Informasi Berdasarkan Tipe Model ---
if isinstance(model, LinearRegression):
    st.markdown("**Jenis Model:** Regresi Linear")
    coef_df = pd.DataFrame({
        "Fitur": ["Open", "High", "Low", "Volume"],
        "Koefisien": model.coef_
    })
    st.table(coef_df)
    st.markdown(f"**Intercept:** `{model.intercept_:.4f}`")

elif isinstance(model, (RandomForestRegressor, GradientBoostingRegressor)):
    st.markdown("**Jenis Model:** Ensemble Tree-Based Regressor")
    feature_df = pd.DataFrame({
        "Fitur": ["Open", "High", "Low", "Volume"],
        "Feature Importance": model.feature_importances_
    }).sort_values(by="Feature Importance", ascending=False)

    st.bar_chart(feature_df.set_index("Fitur"))
else:
    st.warning("Jenis model tidak dikenali.")

# --- Penutup ---
st.markdown("---")
st.info("Model yang dipilih akan digunakan dalam halaman *Formulir Prediksi* untuk memproses input pengguna dan menghasilkan prediksi harga emas.")
