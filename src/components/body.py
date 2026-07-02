import streamlit as st
from src.ui.base_layout import style_base_layout

def teacher_body():
    style_base_layout()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder='@mehnoor')
    teacher_name = st.text_input("Enter name", placeholder='Mehnoor Rahman')
    teacher_password = st.text_input("Enter password", placeholder="Enter your password")
    teacher_password_confirm = st.text_input("Confirm password", placeholder = "Confirm your password")


def teacher_login_body():
    style_base_layout()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder='@mehnoor')
    teacher_password = st.text_input("Enter password", placeholder="Enter your password")