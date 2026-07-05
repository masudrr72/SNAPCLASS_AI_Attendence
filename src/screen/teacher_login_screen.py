import streamlit as st
from src.components.header import header_teacher, subhead_taecher_login
from src.components.body import teacher_login_body
from src.components.footer import footer_teacher
from src.database.db import teacher_login

def teacher_login_screen():

    header_teacher()
    subhead_taecher_login()
    teacher_username, teacher_pass = teacher_login_body()
    st.divider()

    col1, col2 = st.columns(2, gap='small')

    with col1:
        if st.button("Login", shortcut="ctrl+Enter", type='secondary', width='stretch', icon=':material/passkey:'):
            if teacher_login(teacher_username, teacher_pass):
                st.toast("Welcome back!, icon = '👋'")
                import time
                time.sleep(1)
                st.session_state['login_type'] = 'teacher_profile'
                st.rerun()
            else: 
                st.error("Invalid Username and password")             


    with col2:
        if st.button("Register Instead", type='primary', width='stretch', icon=':material/passkey:'):
            st.session_state['login_type'] = 'teacher'
            st.rerun


    footer_teacher()
