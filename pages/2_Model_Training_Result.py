import streamlit as st
import pickle
import os

st.title("📈 Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menampilkan informasi tentang model-machine learning yang telah dilatih untuk memprediksi harga **emas** berdasarkan data historis.

Tiga model yang digunakan:
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

Setiap model dilatih menggunakan fitur:
- Open
- High
- Low
- Volume  
Dengan target prediksi: **Close Price (Harga Penutupan)**.
""")

# Fungsi untuk memuat model
def load_model(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            model = pickle.load(f)
        return model
    else:
        return None

# Load semua model
lr_model = load_model("linear_regression_model.pkl")
rf_model = load_model("random_forest_model.pkl")
gb_model = load_model("gradient_boosting_model.pkl")

# Pilihan model
model_dict = {
    "Linear Regression": lr_model,
    "Random Forest Regressor": rf_model,
    "Gradient Boosting Regressor": gb_model
}

# Dropdown pilih model
selected_model = st.selectbox("Pilih Model untuk Ditampilkan:", list(model_dict.keys()))

model = model_dict[selected_model]

# Tampilkan info model
if model is not None:
    st.success(f"Model {selected_model} berhasil dimuat.")
    
    if selected_model == "Linear Regression":
        st.subheader("Koefisien & Intercept:")
        st.write("**Koefisien:**", model.coef_)
        st.write("**Intercept:**", model.intercept_)
    else:
        st.subheader("Model Tree-Based")
        st.write("Model ini menggunakan pendekatan ensemble berbasis pohon keputusan.")
        st.write("Model sudah siap digunakan untuk prediksi.")

    st.info("Model ini dilatih menggunakan data historis harga emas dan dapat digunakan untuk prediksi harga penutupan berdasarkan input fitur harian.")
else:
    st.error(f"Model {selected_model} tidak ditemukan. Pastikan file dengan nama sesuai berada di direktori utama.")
