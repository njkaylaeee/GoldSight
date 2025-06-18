import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Dataset & Visualisasi")

# Load data
df = pd.read_csv("final_gold_data.csv")
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
