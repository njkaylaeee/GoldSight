import streamlit as st

# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Tampilan popup login
if not st.session_state.logged_in:
    with st.modal("🎉 Selamat Datang!", closable=False):
        st.markdown("Silakan masukkan nama kamu terlebih dahulu!")
        name = st.text_input("Nama Anda", key="name_input")
        if st.button("Masuk"):
            if name.strip():
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip()
                st.rerun()

# Setelah login, tampilkan dashboard
if st.session_state.logged_in:
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Pilih Halaman", ["Main", "Analisis Pasar", "Prediksi Harga", "Edukasi FAQ", "Feedback"])
    st.sidebar.button("Logout", on_click=logout)

    # Konten Halaman Utama
    if menu == "Main":
        st.markdown(f"## 🥇 GoldSight: Navigasi Cerdas Investasi Emas Anda")
        st.markdown(f"### Halo {st.session_state.user_name}! Welcome to Dashboard! 🚀")
        st.markdown("""
        **GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data di tengah volatilitas pasar global. 
        Dengan model GRU dan data historis sejak 2000, kami menyediakan prediksi akurat dan wawasan pasar yang mudah diakses.
        """)

        # Contoh visualisasi
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt

        dummy_data = pd.DataFrame({
            "Tanggal": pd.date_range("2024-01-01", periods=30),
            "Harga": np.random.uniform(2500, 3200, 30)
        })
        st.line_chart(dummy_data.rename(columns={"Tanggal": "index"}).set_index("index"))
