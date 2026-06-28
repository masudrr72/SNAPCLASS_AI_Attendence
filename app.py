import streamlit as st

def main():
    st.header("Welcome Everyone")
    name = st.text_input("Enter your name")
    
    col1, col2 = st.columns(2, gap = 'xlarge')

    with col1:
        if st.button("Hi", type = 'primary', key = 'btn1', width = 'stretch'):
            print("Hi", name)

    with col2:
        if st.button("Bye", type = 'primary', key = 'btn2', width = 'stretch'):
            print("Bye", name)

main()