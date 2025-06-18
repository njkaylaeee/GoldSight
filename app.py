import streamlit as st

st.set_page_config(page_title="GoldSight", page_icon=":bar_chart:", layout="centered")

# --- Simpan status pengguna ---
if 'user_name' not in st.session_state:
    st.session_state.user_name = ""
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

# --- Logo ---
st.image("assets/gold_icon.png", width=120)

# --- Judul ---
st.markdown("""
# **GoldSight**  
#### Navigasi Cerdas Investasi Emas Anda

Prediksi harga emas berbasis deep learning untuk keputusan investasi terbaik.
""")

# --- Tombol buka pop-up ---
if not st.session_state.user_name:
    if st.button("🚀 Go to Dashboard"):
        st.session_state.show_popup = True

# --- Pop-up input nama ---
if st.session_state.show_popup and not st.session_state.user_name:
    with st.form("login_form", clear_on_submit=True):
        name = st.text_input("Masukkan nama Anda:")
        submit = st.form_submit_button("Masuk")
        if submit:
            if name.strip():
                st.session_state.user_name = name.strip().title()
                st.success(f"Halo, {st.session_state.user_name}! Klik tombol di bawah untuk lanjut.")
            else:
                st.warning("Nama tidak boleh kosong.")

# --- Tampilkan tombol lanjut ke dashboard ---
if st.session_state.user_name:
    st.markdown(f"👋 Hai **{st.session_state.user_name}**, selamat datang di GoldSight!")
    st.page_link("pages/1_Data_Exploration.py", label="📊 Buka Dashboard", icon="📈")
