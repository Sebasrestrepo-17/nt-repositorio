import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución")


st.title("Eploracion de Datos con pandas y streamlit")
st.header("Solución")

df = pd.read_csv('integrador\static\estudiantes_colombia.csv')

st.dataframe(df)

st.title("Las primeras 5 filas")
st.dataframe(df.head())

st.title("Las ultimas 5 filas")

st.dataframe(df.tail())

st.title("Mostrar un infrome con: .info()")

st.write(df.info())

st.title("Mostrar las estadisticas basicas con: .describe()")

st.write(df.describe()) 

st.title("Columnas especificas ")

st.write(df[['nombre', 'edad', 'promedio']])



st.title("Filtrar estudiantes con promedio mayor -- Utilizando Slider")
promedio_usuario = st.slider("Promedio", min_value=0, max_value=100, value=75)

st.markdown("</div>", unsafe_allow_html=True)

