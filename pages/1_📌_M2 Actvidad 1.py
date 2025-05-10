import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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


st.header("Actividad #1 -- Creacion de DataFrames")

st.write("Objetivo de la actividad: Demostrar lo aprendido sobre la creacion de Dataframes con Pandas")


st.subheader("Dataframe de Libros -- Diccionario")
Libros = {
    "Nombre": ["El caballero de la armadura oxidada", "El coronel no tiene quien le escriba", "El principito"],
    "Autor" : ["Robert Fisher", "Gabriel García Marquez", "Antoine de Saint-Exupéry"],
    "Año" : ["1991", "1961", "1943"],
    "Genero" : ["Novela", "Novela", "Novela"]
}

df = pd.DataFrame(Libros)
st.dataframe(df)

st.subheader("Dataframe de Informacion de ciudades -- Listas de Diccionarios")
ciudades = [{"Nombre" : "Medellin", "Poblacion" : " 2 533 424", "Pais" : "Colombia"},
            {"Nombre" : "Bogotá", "Poblacion" : "11 795 800", "Pais" : "Colombia"},
            {"Nombre" : "Cali", "Poblacion" : "2 294 653 ", "Pais" : "Colombia"}]

df = pd.DataFrame(ciudades)
st.dataframe(df)
