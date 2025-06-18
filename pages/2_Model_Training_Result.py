# pages/2_Model_Overview.py

import streamlit as st
import pickle
import os

st.set_page_config(page_title="Model Overview", layout="wide")
st.title("📈 Model Prediksi Harga Emas")

st.markdown("""
Selamat datang di halaman _Model Overview_. Di sini Anda dapat melihat informasi terkait model yang telah dilatih untuk memprediksi harga emas berdasarkan data historis.  
Tiga model yang telah digunakan adalah:

- **Linear Regression**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**

Masing-masing model memiliki pendekatan dan keunggulan berbeda dalam menangkap pola data.
""")

st.markdown("---")

# Fungsi untuk menampilkan informasi model
def tampilkan_model(nama_model, filename):
    st.subheader(nama_model)
    if os.path.exists(filename):
        try:
            with open(filename, "rb") as f:
                model = pickle.load(f)
            if hasattr(model, "coef_"):
                st.success("Model berhasil dimuat.")
                st.write("**Koefisien:**", model.coef_)
                st.write("**Intercept:**", model.intercept_)
            elif hasattr(model, "feature_importances_"):
                st.success("Model berhasil dimuat.")
                st.bar_chart(model.feature_importances_)
                st.caption("Grafik di atas menunjukkan pentingnya setiap fitur dalam prediksi.")
            else:
                st.info("Model dimuat, tetapi tidak ada koefisien atau importansi fitur yang tersedia.")
        except Exception as e:
            st.error(f"Gagal memuat model: {e}")
    else:
        st.warning(f"Model **{nama_model}** belum tersedia di direktori.")

# Tampilkan semua model
col1, col2 = st.columns(2)

with col1:
    tampilkan_model("Linear Regression", "linear_regression_model.pkl")
with col2:
    tampilkan_model("Random Forest Regressor", "random_forest_model.pkl")

st.markdown("---")

tampilkan_model("Gradient Boosting Regressor", "gradient_boosting_model.pkl")

st.markdown("""
> **Catatan:**  
> Pastikan seluruh file model `.pkl` telah diunggah ke direktori utama aplikasi (bukan dalam folder) agar dapat terbaca dengan baik.
""")
