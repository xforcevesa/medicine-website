import streamlit as st
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import hasher

config = dict(
    credentials=dict(
        usernames=dict(
            nomodeset=dict(
                email="nomodeset@qq.com",
                name="nomodeset",
                password=hasher.Hasher(["123456789"]).generate()[0]
            )
        )
    ),
    cookie=dict(
        expiry_days=30,
        key="gviufiytfl7t87t7d7coyiv8f87",
        name="kbivufitiyf7i6d77f875ytxutrsy6df8"
    ),
    preauthorized=list(
        "nomodeset@qq.com"
    )
)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)


def render_manage_page():
    st.header('Manage Page')


name, authentication_status, username = authenticator.login(clear_on_submit=True)

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{st.session_state["name"]}*')
    render_manage_page()
elif not st.session_state["authentication_status"]:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')
