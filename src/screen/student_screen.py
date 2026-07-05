import streamlit as st
from PIL import Image
import numpy as np

from src.components.header import header_student, subheader_student
from src.components.footer import footer_dashboard

def student_screen():
    header_student()
    subheader_student()

  
    photo_source = st.camera_input("Position your face in the center")

    if photo_source:
        np.array(Image.open(photo_source))

    footer_dashboard()


    