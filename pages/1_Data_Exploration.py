import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.title("📊 Dataset & Visualisasi")

# Pastikan path-nya sesuai
csv_path = os.path.join(os.path.dirname(__file__), "..", "clean_gold_data.csv")
df = pd.read_csv(csv_path)

st.subheader("Cuplikan Data")
st.dataframe(df.head())

st.subheader("Statistik Deskriptif")
st.write(df.describe())

st.subheader("Visualisasi Harga Emas")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['close'], color='gold', label='Harga Penutupan')
ax.set_title("Tren Harga Emas (Close)")
ax.set_ylabel("Harga")
ax.grid(True)
st.pyplot(fig)
