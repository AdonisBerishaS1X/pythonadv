import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("This is the sidebar")

st.sidebar.selectbox("Choose",["Option1","Option2","Option3"])

st.sidebar.radio("Go TO", ["Home", "Data","Settings"])