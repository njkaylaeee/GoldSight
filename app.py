import streamlit as st

st.set_page_config(page_title="GoldSight", page_icon=":bar_chart:", layout="centered")

# --- Gaya CSS untuk blur saat popup muncul ---
def set_blur():
    st.markdown("""
        <style>
        .blur {
            filter: blur(4px);
            pointer-events: none;
        }
        </style>
    """, unsafe_allow_html=True)

# --- Header Gambar ---
st.image("assets/gold_icon.png", width=120)

# --- Judul dan deskripsi ---
st.markdown("""
# **GoldSight** [Navigasi Cerdas Investasi Emas Anda](#)
#### Prediksi Harga Emas Berbasis Deep Learning

**GoldSight** membantu investor memahami tren harga emas dan membuat keputusan berbasis data di tengah volatilitas pasar global.
""")

# --- Tombol Masuk Dashboard ---
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

if st.button("🚀 Go to Dashboard"):
    st.session_state.show_popup = True

# --- Pop-Up Form Nama ---
if st.session_state.show_popup:
    set_blur()  # Blur background
    with st.container():
        st.markdown("### 🎉 Selamat Datang!")
        name = st.text_input("Silakan masukkan nama kamu terlebih dahulu!", key="name")
        if st.button("Masuk"):
            if name.strip():
                st.success(f"Selamat datang, {name.lower()}! 🎉")
                st.markdown("""<meta http-equiv="refresh" content="2; URL='/pages/1_Dashboard'" />""",
                            unsafe_allow_html=True)
            else:
                st.warning("Nama tidak boleh kosong!")

