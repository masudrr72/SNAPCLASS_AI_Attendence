import streamlit as st
from src.components.header import header_home, subheader_home
from src.ui.base_layout import style_backgroung_home, style_backgroung_dashboard, style_base_layout
from src.components.column import column_teacher, column_student
from src.components.footer import footer_home

def home_screen():
    
    header_home()
    #subheader_home()
    style_backgroung_home()
    style_base_layout()


    col1, col2 = st.columns(2)

    with col1:
        column_student()

        if st.button('Student Portal', type='primary'):
            st.session_state['login_type'] = 'student'
            st.rerun()
 

    with col2:
        column_teacher()
        if st.button('Teacher Portal', type='primary'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()


    footer_home()

