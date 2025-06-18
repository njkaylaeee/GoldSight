import streamlit as st
import pickle
import os

st.title("Model Prediksi Harga Emas")

st.markdown("""
Model yang digunakan pada sistem prediksi ini adalah **Gradient Boosting Regressor**.

Model ini telah dilatih menggunakan fitur:
- `Open`
- `High`
- `Low`
- `Volume`

Dengan target prediksi:
- `Close` (Harga Penutupan Emas)

Gradient Boosting Regressor dikenal memiliki performa yang sangat baik dalam menangani hubungan non-linear dan kompleks antar fitur.
""")

model_path = "models/gradient_boosting_model.pkl"

if os.path.exists(model_path):
    try:
        with open(model_path, "rb") as file:
            model = pickle.load(file)

        st.success("Model Gradient Boosting berhasil dimuat.")

        # Jika model memiliki atribut feature_importances_, tampilkan
        if hasattr(model, "feature_importances_"):
            import pandas as pd
            import matplotlib.pyplot as plt

            fitur = ['Open', 'High', 'Low', 'Volume']
            importances = model.feature_importances_

            df_feat = pd.DataFrame({
                'Fitur': fitur,
                'Pentingnya': importances
            }).sort_values(by='Pentingnya', ascending=False)

            st.subheader("🔍 Pentingnya Fitur (Feature Importance)")
            st.dataframe(df_feat)

            fig, ax = plt.subplots()
            ax.barh(df_feat['Fitur'], df_feat['Pentingnya'], color='gold')
            ax.set_xlabel("Pentingnya")
            ax.set_title("Visualisasi Pentingnya Fitur")
            st.pyplot(fig)

    except Exception as e:
        st.error(f"Gagal memuat model: {e}")
else:
    st.warning(f"File model tidak ditemukan di: `{model_path}`.\n\nPastikan Anda telah mengunggah file `gradient_boosting_model.pkl` ke dalam folder `models/` di GitHub.")
