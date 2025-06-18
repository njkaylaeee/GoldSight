import streamlit as st
import pickle
import os

st.set_page_config(page_title="Model yang Digunakan", layout="wide")

st.title("🧠 Model Prediksi Harga Emas")

st.markdown("""
Pada proyek ini, beberapa model Machine Learning telah dilatih untuk memprediksi harga penutupan (*close*) emas berdasarkan fitur-fitur berikut:

- **Open**: Harga pembukaan
- **High**: Harga tertinggi harian
- **Low**: Harga terendah harian
- **Volume**: Volume perdagangan

Model yang digunakan antara lain:
""")

model_paths = {
    "Linear Regression": "models/linear_regression.pkl",
    "Random Forest Regressor": "models/random_forest.pkl",
    "Gradient Boosting Regressor": "models/gradient_boosting_model.pkl"
}

col1, col2, col3 = st.columns(3)
with col1:
    st.info("🔹 **Linear Regression**\n\nModel sederhana yang mencari hubungan linier antar fitur.")
with col2:
    st.info("🌲 **Random Forest**\n\nKumpulan decision tree yang digabung untuk meningkatkan akurasi.")
with col3:
    st.info("🚀 **Gradient Boosting**\n\nModel canggih yang belajar dari kesalahan model sebelumnya.")

st.markdown("---")

selected_model = st.selectbox("📌 Pilih model untuk melihat detail:", list(model_paths.keys()))
model_file = model_paths[selected_model]

if os.path.exists(model_file):
    with open(model_file, "rb") as f:
        model = pickle.load(f)
    st.success(f"Model **{selected_model}** berhasil dimuat.")

    st.subheader("📊 Informasi Model")

    if hasattr(model, 'coef_'):
        st.markdown("**Koefisien:**")
        st.write(model.coef_)

    if hasattr(model, 'feature_importances_'):
        st.markdown("**Feature Importance:**")
        st.bar_chart(model.feature_importances_)

    if hasattr(model, 'intercept_'):
        st.markdown("**Intercept:**")
        st.write(model.intercept_)

    st.markdown("Model ini siap digunakan untuk prediksi harga emas berdasarkan input pengguna di halaman **Formulir Prediksi**.")
else:
    st.error(f"Model **{selected_model}** tidak ditemukan di path: `{model_file}`.")
    st.markdown("🚨 Silakan periksa apakah file model sudah diunggah ke folder `models/`.")
