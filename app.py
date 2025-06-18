import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Jika belum login, tampilkan modal popup
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        .stApp {
            background-color: rgba(0, 0, 0, 0.5);
        }
        </style>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown("<br><br><br>", unsafe_allow_html=True)
        with st.center():
            with st.container(border=True):
                st.markdown("### 🎉 Selamat Datang!")
                st.write("Silakan masukkan nama kamu terlebih dahulu!")

                name = st.text_input("Nama", key="name_input")

                if st.button("Masuk 🚀"):
                    if name.strip() != "":
                        st.session_state.logged_in = True
                        st.session_state.user_name = name.strip()
                        st.rerun()
                    else:
                        st.warning("Nama tidak boleh kosong.")
else:
    # Sidebar
    st.sidebar.title("GoldSight")
    page = st.sidebar.radio("Navigasi", ["Main", "Analisis Pasar", "Prediksi Harga", "Edukasi FAQ", "Feedback"])
    st.sidebar.button("Logout", on_click=logout)

    # Halaman utama
    if page == "Main":
        st.markdown("## 🥇 **GoldSight: Navigasi Cerdas Investasi Emas Anda**")
        st.markdown(f"### Halo {st.session_state.user_name.lower()}! Welcome to Dashboard! 🚀")
        st.markdown("""
        **GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data di tengah volatilitas pasar global.
        Dengan model GRU dan data historis sejak 2000, kami menyediakan prediksi akurat dan wawasan pasar yang mudah diakses.
        """)

        # Contoh visualisasi dummy
        st.markdown("### Tren Harga Emas Terkini (USD)")
        data = pd.DataFrame({
            "Tanggal": pd.date_range(start="2024-01-01", periods=30),
            "Harga": [2900 + i * 5 + (i % 3) * 30 for i in range(30)]
        })
        fig, ax = plt.subplots()
        ax.plot(data["Tanggal"], data["Harga"], color='blue')
        ax.set_xlabel("Tanggal")
        ax.set_ylabel("Harga Emas (USD)")
        st.pyplot(fig)

    elif page == "Analisis Pasar":
        st.header("📊 Analisis Pasar Emas")
        st.info("Halaman ini akan berisi grafik dan insight pasar emas.")

    elif page == "Prediksi Harga":
        st.header("🔮 Prediksi Harga Emas")
        st.info("Halaman ini akan menampilkan hasil prediksi model GRU.")

    elif page == "Edukasi FAQ":
        st.header("📘 Edukasi dan FAQ")
        st.info("Berisi penjelasan dasar tentang investasi emas dan FAQ.")

    elif page == "Feedback":
        st.header("✍️ Feedback")
        st.text_area("Berikan saran atau pertanyaan:")
        st.button("Kirim")
