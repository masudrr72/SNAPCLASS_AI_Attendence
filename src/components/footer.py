import streamlit as st


def footer_home():
    st.markdown(f"""
        <div style='margin:10rem; display:flex; gap:6px; justify-content:center; item-align:center'>
        
        <p style ="font-weight:bold; color:white">Created With ❤️ by Masudur Rahman</p> 
        </div>      
                """, unsafe_allow_html=True)
    

def footer_dashboard():
    st.markdown(f"""
        <div style='margin:4rem; display:flex; gap:6px; justify-content:center; item-align:center'>
        
        <p style ="font-weight:bold; color:black">Created With ❤️ by Masudur Rahman</p> 
        </div>      
                """, unsafe_allow_html=True)
    
