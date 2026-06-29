import streamlit as st

with st.container():
    st.header("Hello, Neighbour")
    st.write("this is inside the container")

st.write("this is outside the container")