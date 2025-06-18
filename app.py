import streamlit as st
import streamlit.components.v1 as components

# Inisialisasi session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# Fungsi logout
def logout():
    st.session_state.logged_in = False
    st.session_state.user_name = ""

# Tampilan modal login
def show_login():
    st.markdown("""
        <style>
        .overlay {
            position: fixed;
            top: 0; left: 0;
            width: 100vw;
            height: 100vh;
            background-color: rgba(0,0,0,0.5);
            z-index: 1000;
        }
        .modal {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            border-radius: 10px;
            padding: 30px;
            width: 400px;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
            z-index: 1001;
            text-align: center;
        }
        input {
            padding: 10px;
            width: 90%;
            margin-bottom: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
        }
        button {
            padding: 10px 20px;
            background-color: #4CAF50;
            border: none;
            color: white;
            border-radius: 6px;
            cursor: pointer;
        }
        </style>
    """, unsafe_allow_html=True)

    name = st.text_input("Nama Anda", key="login_name")

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("Masuk"):
            if name.strip() == "":
                st.warning("Nama tidak boleh kosong.")
            else:
                st.session_state.logged_in = True
                st.session_state.user_name = name.strip().capitalize()
                st.rerun()

    # Overlay transparan seperti modal
    components.html(f"""
        <div class="overlay"></div>
        <div class="modal">
            <h2>🎉 Selamat Datang!</h2>
            <p>Silakan masukkan nama kamu terlebih dahulu!</p>
            <form>
                <input placeholder="Nama Anda" id="nama" />
                <br/>
                <button onclick="window.parent.postMessage({{type: 'submit'}}, '*')">Masuk</button>
            </form>
        </div>
    """, height=300)

# Tampilan dashboard
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
