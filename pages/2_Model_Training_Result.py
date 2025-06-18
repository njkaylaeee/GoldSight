# pages/2_Model_Overview.py

import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Model Overview", layout="wide")
st.title("📈 Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menyajikan ringkasan dari tiga model pembelajaran mesin yang telah dilatih untuk memprediksi harga emas berdasarkan fitur historis seperti **Open**, **High**, **Low**, dan **Volume**.

Model yang digunakan:
- **Linear Regression**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
""")

st.markdown("---")

# Load dataset uji
@st.cache_data
def load_test_data():
    if os.path.exists("clean_gold_data.csv"):
        df = pd.read_csv("clean_gold_data.csv")
        features = df[['open', 'high', 'low', 'volume']]
        target = df['close']
        return features, target
    return None, None

X_test, y_test = load_test_data()

# Fungsi evaluasi model
def evaluate_model(model, X, y):
    y_pred = model.predict(X)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return mse, r2

# Fungsi untuk memuat dan evaluasi model
def load_and_evaluate_model(name, filename):
    if os.path.exists(filename):
        with open(filename, "rb") as f:
            model = pickle.load(f)
        mse, r2 = evaluate_model(model, X_test, y_test)
        return {"Model": name, "MSE": mse, "R² Score": r2}, model
    return {"Model": name, "MSE": None, "R² Score": None}, None

# List model
model_info = []
models = {
    "Linear Regression": "linear_regression_model.pkl",
    "Random Forest Regressor": "random_forest_model.pkl",
    "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
}

model_objects = {}

for name, path in models.items():
    info, model_obj = load_and_evaluate_model(name, path)
    model_info.append(info)
    model_objects[name] = model_obj

# Tampilkan tabel performa
df_eval = pd.DataFrame(model_info)
st.subheader("📊 Evaluasi Performa Model")
st.dataframe(df_eval.style.format({"MSE": "{:.2f}", "R² Score": "{:.4f}"}), use_container_width=True)

# Visualisasi grafik batang
st.subheader("🔍 Perbandingan Performa Model")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Mean Squared Error (MSE)**")
    st.bar_chart(df_eval.set_index("Model")["MSE"])

with col2:
    st.markdown("**R² Score**")
    st.bar_chart(df_eval.set_index("Model")["R² Score"])

# Tambahkan detail model jika dipilih
st.markdown("---")
st.subheader("📌 Detail Koefisien / Feature Importances")

for name, model in model_objects.items():
    with st.expander(name):
        if model:
            if hasattr(model, "coef_"):
                st.write("**Koefisien:**")
                coef_df = pd.DataFrame({
                    "Fitur": X_test.columns,
                    "Koefisien": model.coef_
                })
                st.table(coef_df)
            elif hasattr(model, "feature_importances_"):
                st.write("**Feature Importances:**")
                importances_df = pd.DataFrame({
                    "Fitur": X_test.columns,
                    "Importance": model.feature_importances_
                }).sort_values(by="Importance", ascending=False)
                st.bar_chart(importances_df.set_index("Fitur"))
        else:
            st.warning("Model belum tersedia.")

st.markdown("""
> **Catatan:**  
> Dataset `clean_gold_data.csv` digunakan sebagai data uji. Pastikan file ini berada di direktori utama bersama file model `.pkl`.
""")
