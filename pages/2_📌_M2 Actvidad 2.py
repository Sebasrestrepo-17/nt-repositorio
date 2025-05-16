import streamlit as st
import pandas as pd
import io

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


st.subheader("Exploración de Datos con pandas y Streamlit")

# Ruta corregida al archivo CSV en la carpeta assets
df = pd.read_csv("assets/datos/estudiantes_colombia.csv")

# Mostrar las primeras 5 filas
st.subheader("Primeras 5 filas del dataset")
st.write(df.head())

# Mostrar las últimas 5 filas
st.subheader("Últimas 5 filas del dataset")
st.write(df.tail())

# Información general del dataset
st.subheader("Información del dataset (.info())")
buffer = io.StringIO()
df.info(buf=buffer)
st.text(buffer.getvalue())

# Estadísticas descriptivas
st.subheader("Estadísticas descriptivas (.describe())")
st.write(df.describe())

# Mostrar columnas específicas
st.subheader("Columnas específicas: nombre, edad y promedio")
st.write(df[["nombre", "edad", "promedio"]])

# Filtrar estudiantes por promedio con slider
st.subheader("Filtrar estudiantes con promedio mayor a un valor")
promedio_usuario = st.slider("Selecciona el promedio mínimo:", min_value=0, max_value=100, value=75)
filtrados = df[df["promedio"] > promedio_usuario]
st.write(f"Estudiantes con promedio mayor a {promedio_usuario}:")
st.write(filtrados)
