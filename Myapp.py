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

plt.style.use("ggplot")

data = {
    "num":[x for x in range(1,11)],
    "square":[x**2 for x in range(1,11)],
    "twice":[x*2 for x in range(1,11)],
    "thrice":[x*3 for x in range(1,11)]
}
rad =st.sidebar.radio("Navigation",["Home","About Us"])

if rad == "Home":
    df = pd.DataFrame(data = data)

    col = st.sidebar.multiselect("Select a Column",df.columns)

    plt.plot(df['num'],df[col])

    st.pyplot()

if rad == "About Us":

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)    

    st.balloons()

    st.error("Error")
    st.success("Show Success")
    st.info("Information")
    st.exception(RuntimeError("this is an error"))
    st.warning("this is a warning")
    
