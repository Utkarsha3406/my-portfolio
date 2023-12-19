import streamlit as st
import pandas
#pandas is third pardy libraries used to read csv data
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

st.write("Below you can find some of the apps I have built in python.Feel free to contact me")
col3,col4=st.columns(2)

df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index ,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index ,row in df[10:].iterrows():
        st.header(row["title"])