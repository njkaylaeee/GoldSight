import streamlit as st

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Halaman login
def show_login():
    st.markdown("<h1 style='text-align: center;'>Selamat Datang di GoldSight</h1>", unsafe_allow_html=True)
    st.write("Silakan masukkan nama Anda untuk mengakses dashboard.")
    
    with st.form("login_form", clear_on_submit=True):
        name = st.text_input("Nama:")
        submit = st.form_submit_button("Masuk")
        if submit:
            if name.strip() == "":
                st.warning("Nama tidak boleh kosong.")
            else:
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip().capitalize()
                st.rerun()

# Halaman utama setelah login
def show_dashboard():
    st.sidebar.title("Navigasi")
    st.sidebar.markdown(f"Selamat datang, **{st.session_state.user_name}**")
    st.sidebar.button("Keluar", on_click=logout)

    st.markdown(f"## Selamat datang, {st.session_state.user_name}")
    st.write("Silakan gunakan menu di sebelah kiri untuk menjelajahi konten dashboard.")

# Routing utama
if not st.session_state.logged_in:
    show_login()
else:
    show_dashboard()
