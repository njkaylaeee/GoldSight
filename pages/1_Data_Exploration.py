import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dataset & Visualisasi", layout="wide")

st.title("📊 Dataset dan Visualisasi Harga Emas")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("final_gold_data.csv")

df = load_data()

# Tampilkan data
st.subheader("🔍 Cuplikan Dataset")
with st.expander("Lihat Data Mentah"):
    st.dataframe(df, use_container_width=True)

# Pilih kolom untuk analisis
st.subheader("📈 Statistik Deskriptif")
selected_columns = st.multiselect(
    "Pilih Kolom untuk Melihat Statistik",
    options=df.select_dtypes(include='number').columns.tolist(),
    default=["open", "high", "low", "close"]
)

if selected_columns:
    st.write(df[selected_columns].describe())

# Visualisasi tren harga emas
st.subheader("📉 Visualisasi Tren Harga Emas")
price_metric = st.selectbox(
    "Pilih Metode Harga yang Ingin Ditampilkan",
    options=["open", "high", "low", "close"],
    index=3
)

fig = px.line(df, y=price_metric, title=f"Tren Harga Emas: {price_metric.upper()}", labels={price_metric: "Harga"})
st.plotly_chart(fig, use_container_width=True)

# Distribusi kolom numerik
st.subheader("📊 Distribusi Kolom Numerik")
dist_col = st.selectbox("Pilih Kolom untuk Distribusi Histogram", options=df.select_dtypes(include='number').columns)
fig_hist = px.histogram(df, x=dist_col, nbins=50, title=f"Distribusi Nilai: {dist_col}")
st.plotly_chart(fig_hist, use_container_width=True)

# Korelasi antar fitur
with st.expander("🧮 Lihat Korelasi Antar Fitur"):
    corr = df.corr(numeric_only=True)
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto", title="Matriks Korelasi")
    st.plotly_chart(fig_corr, use_container_width=True)
