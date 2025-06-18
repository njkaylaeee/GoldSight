import streamlit as st
import pickle

st.title("🧠 Model yang Digunakan")

st.markdown("""
Model yang digunakan dalam prediksi harga emas adalah **Linear Regression**.\n
Model ini dilatih menggunakan fitur:
- Open
- High
- Low
- Volume

Target prediksinya adalah harga **Close**.
""")

# Load model dan tampilkan info
try:
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    st.success("Model berhasil dimuat.")
    st.write("Koefisien:", model.coef_)
    st.write("Intercept:", model.intercept_)
except:
    st.error("Gagal memuat model. Pastikan file model.pkl tersedia.")
