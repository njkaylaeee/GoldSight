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

# Tampilan awal (simulasi modal)
if not st.session_state.logged_in:
    st.markdown("""
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%;
                    background-color: rgba(0, 0, 0, 0.6); display: flex;
                    justify-content: center; align-items: center; z-index: 9999;">
            <div style="background-color: white; padding: 2rem 3rem; border-radius: 1rem;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); text-align: center;">
                <h2>🎉 Selamat Datang!</h2>
                <p>Silakan masukkan nama kamu terlebih dahulu!</p>
                <form action="" method="post">
                    <input name="user_input" id="user_input" placeholder="Nama Anda"
                        style="padding: 0.5rem 1rem; font-size: 1rem; width: 100%; margin-bottom: 1rem;" />
                    <button type="submit" style="padding: 0.5rem 2rem; background-color: #4CAF50;
                        color: white; border: none; border-radius: 0.3rem; font-size: 1rem;">
                        Masuk
                    </button>
                </form>
            </div>
        </div>
    """, unsafe_allow_html=True)

    name = st.text_input("Nama Anda", key="name_input", label_visibility="collapsed")
    if name:
        st.session_state.logged_in = True
        st.session_state.user_name = name.strip()
        st.experimental_rerun()

# Jika sudah login
if st.session_state.logged_in:
    # Sidebar Navigasi
    st.sidebar.title("Navigasi")
    menu = st.sidebar.radio("Pilih Halaman", ["Main", "Analisis Pasar", "Prediksi Harga", "Edukasi FAQ", "Feedback"])
    st.sidebar.button("Logout", on_click=logout)

    # Halaman Utama
    if menu == "Main":
        st.markdown("## 🥇 GoldSight: Navigasi Cerdas Investasi Emas Anda")
        st.markdown(f"### Halo {st.session_state.user_name}! Welcome to Dashboard! 🚀")
        st.markdown("""
        **GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data
        di tengah volatilitas pasar global. Dengan model GRU dan data historis sejak 2000, kami menyediakan
        prediksi akurat dan wawasan pasar yang mudah diakses.
        """)

        # Contoh grafik dummy
        import pandas as pd
        import numpy as np
        dummy_data = pd.DataFrame({
            "Tanggal": pd.date_range("2024-01-01", periods=30),
            "Harga": np.random.uniform(2500, 3200, 30)
        })
        st.line_chart(dummy_data.rename(columns={"Tanggal": "index"}).set_index("index"))
