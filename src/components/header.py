import streamlit as st


def header_home():
    logo_url = "https://i.ibb.co.com/G3rq37Jn/AUTOMATED-4.png" 
    st.markdown(f"""
        <div style='text-align:center; margin-bottom:0px; margin-top:10px;'>
            <img src='{logo_url}' style='height:100px;' />
            <h1 style='text-align:center; color:#E0E3FF'>SNAP<br/>CLASS</h1>
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