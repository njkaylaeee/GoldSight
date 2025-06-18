import streamlit as st
import pickle
import os

st.title("📘 Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menampilkan detail dari beberapa model machine learning yang telah dilatih untuk memprediksi harga emas berdasarkan fitur:
- **Open**
- **High**
- **Low**
- **Volume**

Target prediksi: **Close Price** (Harga Penutupan)
""")

# Menyediakan pilihan model
model_options = {
    "Linear Regression": "models/linear_regression.pkl",
    "Random Forest Regressor": "models/random_forest.pkl",
    "Gradient Boosting Regressor": "models/gradient_boosting.pkl"
}

selected_model = st.selectbox("Pilih Model:", list(model_options.keys()))

model_path = model_options[selected_model]

if os.path.exists(model_path):
    with open(model_path, "rb") as file:
        model = pickle.load(file)

    st.success(f"Model **{selected_model}** berhasil dimuat.")

    if selected_model == "Linear Regression":
        st.subheader("Koefisien Model:")
        st.write(model.coef_)
        st.subheader("Intercept:")
        st.write(model.intercept_)

    else:
        st.subheader("Fitur Penting (Feature Importance):")
        import matplotlib.pyplot as plt
        import pandas as pd
        feature_names = ['Open', 'High', 'Low', 'Volume']
        importance = model.feature_importances_

        fig, ax = plt.subplots()
        ax.barh(feature_names, importance, color='teal')
        ax.set_xlabel("Tingkat Kepentingan")
        ax.set_title("Feature Importance")
        st.pyplot(fig)

else:
    st.error(f"Model `{selected_model}` tidak ditemukan di path: `{model_path}`.")
