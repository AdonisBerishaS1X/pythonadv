import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5,gap="small",vertical_alignment="center")

with col1:
    st.header("kolona 1")
    st.write("Content for column 1")

with col2:
    st.header("Second")
    st.write("Content for Second")

with col3:
    st.header("Third")
    st.write("Content for Third")

with col4:
    st.header("Fourth")
    st.write("Content for Fourth")

with col5:
    st.header("Fifth")
    st.write("Content for Fifth")