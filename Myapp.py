import streamlit as st
st. title("mi pirmer app")
#st.button("dale click")
#st.button("otro boton")
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/data.csv')

st.write(df)

st.map(df)