import streamlit as st
from src.components.header import header_teacher, subhead_teacher
from src.components.body import teacher_body
from src.components.footer import footer_teacher

def teacher_screen():
    header_teacher()
    subhead_teacher()
    teacher_body()
    st.divider()


    col1,col2 = st.columns(2, gap='small')

    with col1:
        if st.button("Register Now", type='primary', shortcut='Shift+Enter', width='stretch', icon=':material/passkey:'):
             st.session_state['login_type'] = 'teacher_profile'
             st.rerun()


    with col2:
        if st.button("Login Instead", type='secondary', width='stretch', icon=':material/passkey:'):
             st.session_state['login_type'] = 'teacher_login'
             st.rerun


    footer_teacher()