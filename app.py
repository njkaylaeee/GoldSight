import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Inisialisasi session state
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""

# Fungsi Logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Tampilan awal: Modal input nama
if not st.session_state.logged_in:
    with st.container():
        st.markdown("""
            <style>
            .big-font {
                font-size:28px !important;
                text-align: center;
            }
            .centered {
                display: flex;
                justify-content: center;
                align-items: center;
            }
            </style>
        """, unsafe_allow_html=True)

        with st.modal("🚀 Selamat Datang di GoldSight", closable=False):
            st.markdown("### Masukkan Nama Anda untuk Memulai")
            name = st.text_input("Nama Lengkap")
            if st.button("Masuk"):
                if name.strip() != "":
                    st.session_state.logged_in = True
                    st.session_state.user_name = name.strip().capitalize()
                    st.rerun()
                else:
                    st.warning("Nama tidak boleh kosong!")

# Tampilan utama setelah login
else:
    # Sidebar hanya muncul jika sudah login
    st.sidebar.title("📊 Navigasi")
    page = st.sidebar.radio("Pilih Halaman:", [
        "Beranda",
        "Analisis Dataset",
        "Hasil Model",
        "Prediksi Harga",
        "Tentang & FAQ"
    ])
    st.sidebar.button("🚪 Logout", on_click=logout)

    # Halaman Beranda
    if page == "Beranda":
        st.markdown(f"## 👋 Selamat datang, {st.session_state.user_name}!")
        st.write("Selamat menjelajahi dashboard **GoldSight**.")
        st.markdown("""
            GoldSight adalah aplikasi analisis harga emas dan prediksi berbasis machine learning
            untuk membantu investor memahami tren dan membuat keputusan cerdas.
        """)
        st.image("https://cdn.pixabay.com/photo/2020/08/13/14/32/gold-5489486_1280.jpg", use_column_width=True)

    elif page == "Analisis Dataset":
        st.header("📊 Analisis Dataset Harga Emas")
        df = pd.read_csv("final_gold_data.csv")

        st.subheader("Cuplikan Data")
        st.dataframe(df.head())

        st.subheader("Statistik Deskriptif")
        st.write(df.describe())

        if 'close' in df.columns:
            st.subheader("Visualisasi Harga Penutupan Emas")
            fig, ax = plt.subplots()
            ax.plot(df['close'], label='Harga Penutupan', color='gold')
            ax.set_xlabel("Index Waktu")
            ax.set_ylabel("Harga (USD)")
            ax.set_title("Tren Harga Penutupan Emas")
            ax.legend()
            st.pyplot(fig)
        else:
            st.warning("Kolom 'close' tidak tersedia di dataset.")

    elif page == "Hasil Model":
        st.header("🧠 Hasil Pelatihan Model")
        st.write("Halaman ini akan menampilkan evaluasi model (akurasi, loss, dll).")
        st.info("Silakan tambahkan visualisasi metrik model di sini.")

    elif page == "Prediksi Harga":
        st.header("📈 Prediksi Harga Emas")
        st.write("Formulir input data dan prediksi harga akan ditampilkan di sini.")
        st.info("Implementasi model GRU/ML akan dimuat di sini.")

    elif page == "Tentang & FAQ":
        st.header("📘 Tentang & FAQ")
        st.markdown("""
        **Apa itu GoldSight?**  
        Platform untuk memprediksi harga emas berdasarkan data historis dan sentimen berita.

        **Model apa yang digunakan?**  
        GRU (Gated Recurrent Unit) dengan embedding sentimen dan data historis.

        **Siapa yang bisa menggunakan ini?**  
        Investor, analis, pelajar, atau siapa pun yang tertarik dengan pasar emas.
        """)

        st.success("Terima kasih sudah menggunakan GoldSight!")
