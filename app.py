import streamlit as st

st.header("Calculadora", deliminter="gray")

st.write("Expressão")
expression = st.text_input("Entre com os valores")

if expression:
    result = eval(expression)
    st.write(f"Resultado: {result}")
