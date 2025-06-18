import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Prediksi Harga Emas", layout="centered")
st.title("💰 Prediksi Harga Penutupan Emas")

st.markdown("""
Masukkan data pasar harian di bawah ini, lalu pilih model untuk melihat prediksi harga penutupan emas berdasarkan input Anda.
""")

st.markdown("---")

# Input user
col1, col2 = st.columns(2)
with col1:
    open_price = st.number_input("📥 Open", min_value=0.0, step=0.01)
    low_price = st.number_input("📉 Low", min_value=0.0, step=0.01)
with col2:
    high_price = st.number_input("📈 High", min_value=0.0, step=0.01)
    volume = st.number_input("📊 Volume", min_value=0.0, step=1.0)

# Pilihan model
model_dict = {
    "Linear Regression": "linear_regression_model.pkl",
    "Random Forest Regressor": "random_forest_model.pkl",
    "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
}

selected_model = st.selectbox("🧠 Pilih Model Prediksi", list(model_dict.keys()))
model_path = model_dict[selected_model]

# Tombol prediksi
if st.button("🔮 Prediksi Harga"):
    if not os.path.exists(model_path):
        st.error(f"Model **{selected_model}** tidak ditemukan. Pastikan file `{model_path}` tersedia.")
    else:
        try:
            with open(model_path, "rb") as f:
                model = pickle.load(f)

            input_data = np.array([[open_price, high_price, low_price, volume]])
            prediction = model.predict(input_data)[0]

            st.success(f"✅ Prediksi Berhasil Menggunakan: {selected_model}")
            st.markdown("---")
            st.subheader("📌 Hasil Prediksi")

            st.markdown(f"""
            <div style='
                background-color:#f9f9f9;
                padding:20px;
                border-radius:12px;
                text-align:center;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);'>
                <h2 style='color:gold;'>${prediction:,.2f}</h2>
                <p style='margin-top:-10px;'>Harga Penutupan Emas yang Diprediksi</p>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memuat model: {e}")
