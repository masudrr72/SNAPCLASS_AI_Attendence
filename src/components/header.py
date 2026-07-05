import streamlit as st
from src.ui.base_layout import style_backgroung_dashboard, style_base_layout


def header_home():
    logo_url = "https://i.ibb.co.com/G3rq37Jn/AUTOMATED-4.png" 
    st.markdown(f"""
        <div style='text-align:center; margin-bottom:0px; margin-top:10px;'>
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
        </div>      
                """, unsafe_allow_html=True)

def header_teacher():
    style_backgroung_dashboard()
    style_base_layout()

    col1,col2 = st.columns(2, vertical_alignment='center', gap='xlarge')

    with col1:

        logo_url = "https://i.ibb.co.com/G3rq37Jn/AUTOMATED-4.png"
        st.markdown(f"""
            <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-top:10px;'>
                <img src='{logo_url}' style='height:100px;' />
                <h2 style = 'color:#5865F2;'>SNAP<br/>CLASS</h2>
            </div>      
                    """, unsafe_allow_html=True)
        
    with col2:
        if st.button("Go back to home", type='secondary', key='homebackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None


def subhead_teacher():
    st.markdown(f"""
    <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-top:0px;'>
        <h2 style = 'color:black;'>Register your teacher profile</h2>
    </div>      
            """, unsafe_allow_html=True)
    


def subhead_taecher_login():
    st.markdown(f"""
    <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-top:0px;'>
        <h2 style = 'color:black;'>Login your teacher profile</h2>
    </div>      
            """, unsafe_allow_html=True)
    
def subhead_taecher_profile():
    st.markdown(f"""
    <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-top:0px;'>
        <h2 style = 'color:black;'>Welcome to your teacher profile</h2>
    </div>      
            """, unsafe_allow_html=True)

    


def header_student():
    style_backgroung_dashboard()
    style_base_layout()

    col1,col2 = st.columns(2, vertical_alignment='center', gap='xlarge')

    with col1:

        logo_url = "https://i.ibb.co.com/G3rq37Jn/AUTOMATED-4.png"
        st.markdown(f"""
            <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin-top:10px;'>
                <img src='{logo_url}' style='height:100px;' />
                <h2 style = 'color:#5865F2;'>SNAP<br/>CLASS</h2>
            </div>      
                    """, unsafe_allow_html=True)
    with col2:
        if st.button("Go back to home", type='secondary', key='homebackbtn', shortcut="control+backspace"):
            st.session_state['login_type'] = None


def subheader_student():
    st.markdown(f"""
    <div style='display:flex; align-items:center; justify-content:center; gap:10px; margin:30px;'>
        <h2 style = 'color:black;'>Login with FaceID</h2>
    </div>      
            """, unsafe_allow_html=True)



def subheader_home():
    st.markdown("""
    <style>

    .hero-section{
        max-width:850px;
        margin:0 auto 35px auto;
        text-align:center;
        color:white;
        font-family:'Poppins', sans-serif;
    }

    /* Heading */
    .hero-title{
        font-size:32px;
        font-weight:700;
        line-height:1.4;
    }

    .hero-title .brand{
        color:#FFC83D;
    }

    .hero-title .ai{
        color:#5EE7FF;
        font-style:italic;
    }

    /* Description */
    .hero-desc{
        margin-top:12px;
        font-size:17px;
        color:#E5E7FF;
        line-height:1.7;
    }

    .hero-desc .face{
        color:#5EE7FF;
        font-weight:600;
    }

    .hero-desc .voice{
        color:#FFC83D;
        font-weight:600;
    }

    /* Feature Box */

    .feature-box{
        margin-top:25px;
        padding:18px 25px;
        border:1.5px solid rgba(255,255,255,.25);
        border-radius:16px;
        background:rgba(255,255,255,.05);
        backdrop-filter:blur(12px);

        display:flex;
        justify-content:space-around;
        align-items:center;
        flex-wrap:wrap;
    }

    .feature{
        color:white;
        font-size:15px;
        font-weight:500;
    }

    .feature span{
        display:block;
        font-size:28px;
        margin-bottom:6px;
    }

    /* Bottom CTA */

    .cta-box{

        margin:22px auto 0;
        width:78%;

        border:1px solid rgba(255,255,255,.25);
        border-radius:50px;

        padding:10px 20px;

        background:rgba(255,255,255,.05);

        color:#F5F5F5;

        font-size:18px;
        font-style:italic;
    }

    </style>

    <div class="hero-section">

    <div class="hero-title">
    Welcome to <span class="brand">SnapClass</span> –
    Your Smart Classroom, Powered by
    <span class="ai">AI ✨</span>
    </div>

    <div class="hero-desc">

    SnapClass automatically takes attendance using
    <span class="face">Face Recognition</span> and
    <span class="voice">Voice Recognition</span>,
    making every class faster, smarter, and more reliable.

    </div>

    <div class="feature-box">

    <div class="feature">
    <span>📸</span>
    AI-Powered<br>Attendance
    </div>

    <div class="feature">
    <span>🎤</span>
    Voice<br>Recognition
    </div>

    <div class="feature">
    <span>🛡️</span>
    Accurate &<br>Secure
    </div>

    <div class="feature">
    <span>📈</span>
    Real-time<br>Insights
    </div>

    </div>

    <div class="cta-box">
    Choose your role below and step into a smarter learning experience!
    </div>

    </div>

    """, unsafe_allow_html=True)