# pages/2_Model_Overview.py

import streamlit as st
import pickle
import os
import numpy as np
import pandas as pd

st.set_page_config(page_title="Model Overview", layout="wide")
st.title("📈 Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menyajikan informasi singkat mengenai model yang digunakan untuk memprediksi harga emas.  
Silakan pilih model dari dropdown di bawah untuk melihat detailnya.
""")

st.markdown("---")

# Daftar model
model_options = {
    "Linear Regression": "linear_regression_model.pkl",
    "Random Forest Regressor": "random_forest_model.pkl",
    "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
}

# Dropdown pilih model
selected_model = st.selectbox("🔍 Pilih Model", list(model_options.keys()))

# Fungsi tampilkan model
def tampilkan_model(nama_model, filename):
    st.subheader(f"📌 Detail Model: {nama_model}")

    if not os.path.exists(filename):
        st.warning(f"Model **{nama_model}** belum tersedia di direktori.")
        return

    try:
        with open(filename, "rb") as f:
            model = pickle.load(f)
        st.success("✅ Model berhasil dimuat.")
        
        if hasattr(model, "coef_"):  # Linear Regression
            st.write("**Koefisien Fitur:**")
            coef_df = pd.DataFrame({
                "Fitur": ["Open", "High", "Low", "Volume"],
                "Koefisien": model.coef_
            })
            st.dataframe(coef_df, use_container_width=True)
            st.write("**Intercept:**", model.intercept_)

        elif hasattr(model, "feature_importances_"):  # Tree-based
            st.write("**Feature Importance:**")
            fitur = ["Open", "High", "Low", "Volume"]
            importance = model.feature_importances_
            importance_df = pd.DataFrame({
                "Fitur": fitur,
                "Importance": importance
            }).sort_values(by="Importance", ascending=False)
            st.bar_chart(importance_df.set_index("Fitur"))
            st.caption("Grafik menunjukkan seberapa besar kontribusi masing-masing fitur terhadap prediksi.")
        
        else:
            st.info("Model dimuat, namun tidak memiliki atribut koefisien atau feature importance.")

    except Exception as e:
        st.error(f"❌ Gagal memuat model: {e}")

# Tampilkan model terpilih
tampilkan_model(selected_model, model_options[selected_model])
