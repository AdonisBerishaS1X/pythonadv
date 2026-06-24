import streamlit as st
from numpy.random.mtrand import operator


def calculate(numer1, numer2, operator):

    if operator=="mbledh":
        rez=numer1 +numer2
    elif operator =="zbritje":
        rez=numer1 -numer2
    elif operator =="shummezim":
        rez=numer1*numer2
    elif operator =="pjestim":
        try:
            rez=numer1 / numer2
        except ZeroDivisionError:
            rez="Cant divide with 0"


    return rez


def main():
    st.title("Calculate")

    num1 = st.number_input("Write the first number")

    num2 = st.number_input("Write the second number")

    operatori= st.radio("Select operator", ["mbledhje","zbritje","shumzim","pjestim"])

    rezultati = calculate(num1,num2,operatori)
    st.write(rezultati)

    if __name__=="__main__":
        main()