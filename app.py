if not st.session_state.logged_in:
    st.markdown(
        """
        <style>
            .overlay {
                position: fixed; top: 0; left: 0;
                width: 100vw; height: 100vh;
                background-color: rgba(0, 0, 0, 0.6);
                display: flex; justify-content: center;
                align-items: center; z-index: 9999;
            }
            .login-box {
                background-color: white;
                padding: 2rem 3rem;
                border-radius: 1rem;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.3);
                text-align: center;
                max-width: 400px;
                width: 100%;
            }
        </style>
        <div class="overlay">
            <div class="login-box">
                <h2>🎉 Selamat Datang!</h2>
                <p>Silakan masukkan nama kamu terlebih dahulu!</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Letakkan input dan tombol DI LUAR markdown tapi secara visual tetap dalam konteks modal
    name = st.text_input("Nama kamu", key="name_input")
    if st.button("Masuk"):
        if name.strip():
            st.session_state.user_name = name.strip()
            st.session_state.logged_in = True
        else:
            st.warning("Nama tidak boleh kosong.")
    
    st.stop()  # Hentikan sisa halaman sebelum login
