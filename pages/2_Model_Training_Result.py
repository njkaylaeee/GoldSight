import streamlit as st
import pickle
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Hasil Pelatihan Model", layout="wide")
st.title("📈 Hasil Pelatihan Model Prediksi Harga Emas")

st.markdown("""
Halaman ini menampilkan performa dari beberapa model Machine Learning yang telah dilatih untuk memprediksi harga penutupan (close) emas berdasarkan fitur:
- Open
- High
- Low
- Volume

Setiap model dibandingkan berdasarkan akurasi prediksi (R²) dan galat kuadrat rata-rata (MSE).
""")

# Fungsi load scaler
@st.cache_resource
def load_scaler():
    try:
        with open("scaler.pkl", "rb") as f:
            return pickle.load(f)
    except:
        return None

# Load data uji
@st.cache_data
def load_test_data():
    df = pd.read_csv("clean_gold_data.csv")
    X = df[['open', 'high', 'low', 'volume']]
    y = df['close']
    return X, y

# Evaluasi model
def evaluate_model(model, X, y):
    scaler = load_scaler()
    if scaler:
        X_scaled = scaler.transform(X)
    else:
        X_scaled = X
    y_pred = model.predict(X_scaled)
    mse = mean_squared_error(y, y_pred)
    r2 = r2_score(y, y_pred)
    return mse, r2, y_pred

# Load & evaluasi model
def load_model_and_evaluate(name, path, X, y):
    try:
        with open(path, "rb") as f:
            model = pickle.load(f)
        mse, r2, y_pred = evaluate_model(model, X, y)
        return model, mse, r2, y_pred
    except Exception as e:
        st.error(f"❌ Gagal memuat model {name}: {e}")
        return None, None, None, None

# Model paths
model_paths = {
    "Linear Regression": "linear_regression_model.pkl",
    "Random Forest Regressor": "random_forest_model.pkl",
    "Gradient Boosting Regressor": "gradient_boosting_model.pkl"
}

X_test, y_test = load_test_data()

st.divider()
st.subheader("📊 Perbandingan Performa Model")

results = []

for model_name, model_file in model_paths.items():
    model, mse, r2, y_pred = load_model_and_evaluate(model_name, model_file, X_test, y_test)
    if model:
        results.append({"Model": model_name, "MSE": mse, "R2": r2})

# Tampilkan tabel hasil evaluasi
if results:
    result_df = pd.DataFrame(results).sort_values(by="R2", ascending=False)
    st.dataframe(result_df.style.background_gradient(cmap='YlGn'), use_container_width=True)

    # Visualisasi perbandingan R²
    st.subheader("📈 Visualisasi R² Setiap Model")
    fig_r2, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x="R2", y="Model", data=result_df, palette="viridis", ax=ax)
    ax.set_title("Skor R² per Model")
    ax.set_xlim(0, 1)
    st.pyplot(fig_r2)

    # Visualisasi prediksi vs aktual untuk model terbaik
    best_model_row = result_df.iloc[0]
    best_name = best_model_row['Model']
    _, _, _, best_pred = load_model_and_evaluate(best_name, model_paths[best_name], X_test, y_test)

    st.subheader(f"🔍 Prediksi vs Aktual - {best_name}")
    fig_line, ax = plt.subplots(figsize=(10, 4))
    ax.plot(y_test.values, label='Aktual', color='blue')
    ax.plot(best_pred, label='Prediksi', color='orange')
    ax.set_title(f"Prediksi vs Aktual Harga Penutupan oleh {best_name}")
    ax.set_ylabel("Harga Emas")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig_line)
else:
    st.warning("⚠️ Tidak ada model yang berhasil dimuat. Pastikan file model tersedia dan sesuai.")
