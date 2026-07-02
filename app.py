import streamlit as st

from src.screen.home_screen import home_screen
from src.screen.teacher_screen import teacher_screen
from src.screen.student_screen import student_screen
from src.screen.teacher_profile_screen import teacher_profile_screen
from src.screen.teacher_login_screen import teacher_login_screen

def main():
    
    if 'login_type' not in st.session_state:
        st.session_state['login_type'] = None

    match st.session_state['login_type']:
        case 'teacher':
            teacher_screen()

        case 'student':
            student_screen()

        case None:
            home_screen()

        case 'teacher_profile':
            teacher_profile_screen()

        case 'teacher_login':
            teacher_login_screen()

main()