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
    st.markdown("<h1 style='text-align: center;'>🌟 Selamat Datang di GoldSight</h1>", unsafe_allow_html=True)
    with st.form("login_form", clear_on_submit=True):
        name = st.text_input("Masukkan Nama Anda:")
        submit = st.form_submit_button("Get Dashboard")
        if submit:
            if name.strip() == "":
                st.warning("Nama tidak boleh kosong.")
            else:
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip().capitalize()
                st.rerun()

# Halaman dashboard setelah login
def show_dashboard():
    st.sidebar.title("🔎 Navigasi")
    st.sidebar.success(f"Hai, {st.session_state.user_name} 👋")
    st.sidebar.button("🚪 Logout", on_click=logout)

    st.markdown(f"## 👋 Selamat datang, {st.session_state.user_name}!")
    st.success("Silakan menjelajahi dashboard menggunakan menu di sebelah kiri.")

# Main routing
if not st.session_state.logged_in:
    show_login()
else:
    show_dashboard()
