import streamlit as st
import pickle
import os
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Model Prediksi", layout="wide")

st.title("📈 Model Prediksi Harga Emas")

# Deskripsi Awal
with st.container():
    st.markdown("""
    Sistem ini menggunakan pendekatan *machine learning* untuk memprediksi harga penutupan emas berdasarkan fitur historis.
    
    Model yang digunakan:  
    ### 🎯 Gradient Boosting Regressor  
    Algoritma ini terkenal efektif dalam menangkap pola kompleks dan memberikan akurasi tinggi pada data non-linear.
    """)

# Cek file model
model_path = "models/gradient_boosting_model.pkl"

if not os.path.exists(model_path):
    st.error(f"Model belum ditemukan di path: `{model_path}`. Pastikan file sudah diunggah.")
    st.stop()

# Load model
with open(model_path, "rb") as file:
    model = pickle.load(file)

st.success("Model berhasil dimuat dan siap digunakan.")

# Ringkasan Informasi Model
with st.expander("📌 Informasi Model", expanded=True):
    st.markdown("""
    **Gradient Boosting Regressor** merupakan ensemble model berbasis pohon keputusan.  
    Model ini dibangun secara bertahap untuk meminimalkan kesalahan prediksi secara iteratif.

    - Jumlah estimators: `100`
    - Random state: `42`
    - Target: `Harga Penutupan (Close)`
    """)

# Tampilkan Feature Importance
if hasattr(model, "feature_importances_"):
    fitur = ['Open', 'High', 'Low', 'Volume']
    importance = model.feature_importances_
    df_feat = pd.DataFrame({'Fitur': fitur, 'Pentingnya': importance})
    df_feat = df_feat.sort_values(by='Pentingnya', ascending=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.metric("Jumlah Fitur", len(fitur))
        st.metric("Fitur Terpenting", df_feat.iloc[-1]['Fitur'])

    with col2:
        st.subheader("🔍 Pentingnya Setiap Fitur")
        fig, ax = plt.subplots()
        ax.barh(df_feat['Fitur'], df_feat['Pentingnya'], color='gold')
        ax.set_xlabel("Pentingnya")
        ax.set_title("Feature Importance")
        st.pyplot(fig)

# Simulasi Penjelasan Hasil
with st.container():
    st.markdown("---")
    st.subheader("📘 Kesimpulan")
    st.markdown("""
    Berdasarkan pelatihan model, fitur yang paling memengaruhi prediksi harga penutupan adalah kombinasi dari harga `Open` dan `High`.
    Dengan performa yang stabil, model ini siap digunakan dalam sistem prediksi emas secara real-time.

    > Anda dapat melanjutkan ke halaman **Prediksi Harga** untuk mencoba model ini dengan data Anda sendiri.
    """)

