from random import choice

import streamlit as st
from watchdog.observers.fsevents2 import message

st.title("hello")

st.button("Click This")

if st.button("Crank It"):
    st.write("You have alerted the horde")

st.checkbox("check me")


if st.checkbox("Cliche"):
    st.write("You have alerted another Horde")

userInput = st.text_input("Emter a text")

st.write("You have alerted: ", userInput)


age = st.number_input("Enter your Horde", min_value=1,max_value=100)

st.write("the number of Hordes you have alerted is", age)


message = st.text_area("Enter a message")

choice = st.radio("pick one", ["Horde","Hoard","Hored"])

st.write(choice)
