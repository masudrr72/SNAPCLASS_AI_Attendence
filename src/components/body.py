import streamlit as st
from src.ui.base_layout import style_base_layout

def teacher_body():
    style_base_layout()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder='@mehnoor',  key="teacher_usernames")
    teacher_name = st.text_input("Enter name", placeholder='Mehnoor Rahman', key="teacher_name")
    teacher_pass = st.text_input("Enter password", placeholder="Enter your password", key="teacher_pass")
    teacher_pass_confirm = st.text_input("Confirm password", placeholder = "Confirm your password", key="teacher_pass_confirm")

    return teacher_username, teacher_name, teacher_pass, teacher_pass_confirm

def teacher_login_body():
    style_base_layout()
    st.space()
    
    teacher_username = st.text_input("Enter username", placeholder='@mehnoor', key="Login_username")
    teacher_pass = st.text_input("Enter password", placeholder="Enter your password", key= "login_password")
    return teacher_username, teacher_pass