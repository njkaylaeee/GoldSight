import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Prediksi Harga Emas", layout="centered")
st.title("💰 Prediksi Harga Penutupan Emas")

st.markdown("Masukkan data pasar dan pilih model prediksi untuk melihat estimasi harga penutupan emas.")

st.markdown("---")

# Tabs untuk Input dan Output
tab1, tab2 = st.tabs(["🧾 Input Data", "📊 Hasil Prediksi"])

with tab1:
    st.subheader("📥 Masukkan Fitur Pasar")
    
    open_price = st.slider("Harga Open", min_value=0.0, max_value=3000.0, value=1900.0, step=0.1)
    high_price = st.slider("Harga High", min_value=0.0, max_value=3000.0, value=1950.0, step=0.1)
    low_price = st.slider("Harga Low", min_value=0.0, max_value=3000.0, value=1850.0, step=0.1)
    volume = st.number_input("Volume Transaksi", min_value=0.0, value=100000.0, step=1000.0)

    selected_model = st.selectbox("🧠 Pilih Model Prediksi", {
        "Linear Regression": "linear_regression_model.pkl",
        "Random Forest Regressor": "random_forest_model.pkl",
        "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
    }.keys())

    if st.button("🔮 Prediksi Sekarang"):
        st.session_state.run_prediction = True
        st.session_state.inputs = (open_price, high_price, low_price, volume)
        st.session_state.model_name = selected_model

# Prediction logic
if st.session_state.get("run_prediction", False):
    with tab2:
        open_price, high_price, low_price, volume = st.session_state.inputs
        selected_model = st.session_state.model_name
        model_file = {
            "Linear Regression": "linear_regression_model.pkl",
            "Random Forest Regressor": "random_forest_model.pkl",
            "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
        }[selected_model]

        st.subheader(f"📈 Hasil Prediksi menggunakan {selected_model}")
        
        if not os.path.exists(model_file):
            st.error(f"Model `{selected_model}` tidak ditemukan.")
        else:
            try:
                with open(model_file, "rb") as f:
                    model = pickle.load(f)
                input_data = np.array([[open_price, high_price, low_price, volume]])
                pred = model.predict(input_data)[0]

                st.success("✅ Prediksi berhasil!")
                st.markdown(f"""
                <div style='
                    background-color:#fff8dc;
                    padding:20px;
                    border-radius:10px;
                    text-align:center;
                    box-shadow:0 0 8px rgba(0,0,0,0.1);'>
                    <h2 style='color:#DAA520;'>${pred:,.2f}</h2>
                    <p>Harga penutupan emas yang diprediksi</p>
                </div>
                """, unsafe_allow_html=True)

                st.caption(f"Fitur yang digunakan: Open = {open_price}, High = {high_price}, Low = {low_price}, Volume = {volume}")

            except Exception as e:
                st.error(f"Terjadi kesalahan saat memuat model: {e}")
