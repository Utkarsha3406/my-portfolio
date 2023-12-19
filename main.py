import streamlit as st
st.set_page_config(layout="wide")
col1,col2 =st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Utkarsha Chore")
    content ="""
    Hi,I am Utkarsha! I am a python programmer,studying in SRM Institute of Science and Technology ,KTR
    graduating in 2025.
    """
    st.info(content)

