import streamlit as st
st. title("mi pirmer app")
click=st.button("dale click")
st.write("el valor de click es:", click)
if click==True:
    st.image("LOGO UACH.png")
#st.button("otro boton")

if click==True:
    st.image("LOGO UACH.png")
import pandas as pd

#1er ejecicio
#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

#st.write(df)

#st.map(df)

#st.text("hola mundo")
#st.text("la siguiente es una integral")
#st.latex("\int_1^6")
#st.markdown("*este es una viñeta*")

num1 = st.slider('Elige un numero 1',0.0,100.0,25.0)
num2 = st.slider('Elige un numero 2',0.0,100.0,25.0)
suma= num1+num2
st.write("la suma de",num1,"y",num2,"es:",suma)

st.write("Ahora multipliquemos")

nn1= st.number_input("dame n1")
nn2= st.number_input("dame n2")
mult= nn1*nn2
st.write("la multiplicacion",nn1,"y",nn2,"es:",mult)

with st.sidebar:
    num1 = st.slider('Elige un numero 1',0.0,100.0,25.0)
    num2 = st.slider('Elige un numero 2',0.0,100.0,25.0)
    suma= num1+num2
    click=st.button("dale click")

    st.write("el valor de click es:", click)
    
    st.markdown("<h1 style='text-align: center; color: red;'>Some title</h1>", unsafe_allow_html=True)
    
