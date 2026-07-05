import streamlit as st
from src.components.header import header_teacher, subhead_teacher
from src.components.body import teacher_body
from src.components.footer import footer_teacher
from src.database.db import check_teacher_exists, create_teacher


def register_teacher(teacher_username, teacher_name, teacher_pass, teacher_pass_confirm):
    if not teacher_username or not teacher_name or not teacher_pass :
        return False, "All fields are requires!"
    
    if check_teacher_exists(teacher_username):
        return False, "Username already taken"

    if teacher_pass != teacher_pass_confirm:
        return False, "password doesn't match"
    
    try: 
        create_teacher(teacher_username, teacher_pass, teacher_name)
        return True, "Successfully created! Login now"

    except Exception as e:
        return False, "Unexpected"


    

def teacher_screen():
    header_teacher()
    subhead_teacher()
    teacher_username, teacher_name, teacher_pass, teacher_pass_confirm = teacher_body()
    st.divider()


    col1,col2 = st.columns(2, gap='small')

    with col1:
        if st.button("Register Now", type='primary', shortcut='Shift+Enter', width='stretch', icon=':material/passkey:'):
            success, message = register_teacher( teacher_username, teacher_name, teacher_pass, teacher_pass_confirm )
            if success: 
                st.success(message)
                import time 
                time.sleep(2)
                st.session_state['login_type'] = 'teacher_profile'
                st.rerun()
            else:
                st.error(message)
                




    with col2:
        if st.button("Login Instead", type='secondary', width='stretch', icon=':material/passkey:'):
             st.session_state['login_type'] = 'teacher_login'
             st.rerun


    footer_teacher()