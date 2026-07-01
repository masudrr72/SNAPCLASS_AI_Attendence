import streamlit as st

def column_teacher():
    teacher_url = "https://i.ibb.co.com/nqjSDTYq/AUTOMATED-3.png"
    st.markdown(f"""
            <div style='margin-bottom:20px; margin-top:10px;'>
                <h2>I'm Teacher</h2>
                <img src='{teacher_url}' style='height:180px;'/>
                
            </div>

                """, unsafe_allow_html= True)
    

def column_student():
    student_url = "https://i.ibb.co.com/GLgXM8P/AUTOMATED-2.png"
    st.markdown(f"""
            <div style='margin-bottom:20px; margin-top:10px;'>
                <h2>I'm Student</h2>
                <img src='{student_url}' style='height:180px;'/>
                
            </div>

                """, unsafe_allow_html= True)