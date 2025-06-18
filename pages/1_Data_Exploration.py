import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Dataset & Visualisasi")

# Pastikan path-nya relatif ke root folder
df = pd.read_csv("final_gold_data.csv")

st.subheader("Cuplikan Data")
st.dataframe(df.head())
