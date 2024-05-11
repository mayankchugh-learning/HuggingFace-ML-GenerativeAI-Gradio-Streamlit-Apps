import streamlit as st
st.write('# Streamlit calculator')
number1= st.number_input('number 1')
number2 = st.number_input('number 2')
num3 = number1+number2
st.write('# Answer is ',num3)