import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.write("this is inside sidebar")

st.sidebar.selectbox("choose options",["Option 1","Opt2","Opt3",])

st.sidebar.radio("Go to",["Home","Data","Settings"])