import streamlit as st
import pandas as pd
import numpy as np

# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Fungsi login (dengan nama)
def login():
    name = st.session_state.name_input.strip()
    if name != "":
        st.session_state.user_name = name
        st.session_state.logged_in = True

# Tampilan "Popup" Login Simulasi
if not st.session_state.logged_in:
    with st.container():
        st.markdown(
            """
            <style>
                .overlay {
                    position: fixed; top: 0; left: 0;
                    width: 100vw; height: 100vh;
                    background-color: rgba(0, 0, 0, 0.5);
                    display: flex; justify-content: center;
                    align-items: center; z-index: 9999;
                }
                .login-box {
                    background-color: white; padding: 2rem 3rem;
                    border-radius: 1rem;
                    box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
                    text-align: center;
                    width: 100%;
                    max-width: 400px;
                }
            </style>
            <div class="overlay">
                <div class="login-box">
                    <h2>🎉 Selamat Datang!</h2>
                    <p>Silakan masukkan nama kamu terlebih dahulu!</p>
            """,
            unsafe_allow_html=True
        )
        st.text_input("Nama Anda", key="name_input", label_visibility="collapsed")
        if st.button("Masuk"):
            login()
        st.markdown("</div></div>", unsafe_allow_html=True)
    st.stop()  # Hentikan eksekusi hingga login berhasil

# Jika sudah login, tampilkan dashboard
st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Main", "Analisis Pasar", "Prediksi Harga", "Edukasi FAQ", "Feedback"])
st.sidebar.button("Logout", on_click=logout)

if menu == "Main":
    st.markdown("## 🥇 GoldSight: Navigasi Cerdas Investasi Emas Anda")
    st.markdown(f"### Halo {st.session_state.user_name}! Welcome to Dashboard! 🚀")
    st.markdown("""
    **GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data
    di tengah volatilitas pasar global. Dengan model GRU dan data historis sejak 2000, kami menyediakan
    prediksi akurat dan wawasan pasar yang mudah diakses.
    """)
    
    # Grafik dummy tren emas
    dummy_data = pd.DataFrame({
        "Tanggal": pd.date_range("2024-01-01", periods=30),
        "Harga": np.random.uniform(2500, 3200, 30)
    })
    st.line_chart(dummy_data.rename(columns={"Tanggal": "index"}).set_index("index"))
