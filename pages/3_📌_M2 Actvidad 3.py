import streamlit as st
import pandas as pd
from datetime import date

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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

st.subheader("Actividad #3 -- Google Colab")
st.markdown("[Abrir en Google Colab](https://colab.research.google.com/drive/1tKo89cvTVSJCFmutkkU4fHbxG_C7K2TF?usp=sharing)")


df = pd.read_csv("assets/datos/datos.csv", parse_dates=["fecha_nacimiento"])

st.subheader("Actividad #3 -- Python/Streamlit")


# Copia del DataFrame para aplicar filtros
df_filtrado = df.copy()

st.sidebar.header("Filtros")

# 1. Filtro por rango de edad
if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (18, 60))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

# 2. Filtro por municipios
if st.sidebar.checkbox("Filtrar por municipios"):
    municipios_opciones = df['municipio'].dropna().unique().tolist()
    municipios = st.sidebar.multiselect("Selecciona los municipios", municipios_opciones)
    if municipios:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios)]

# 3. Filtro por ingreso mensual mínimo
if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_min = st.sidebar.slider("Ingreso mínimo (COP)", 800000, 12000000, 3000000, step=100000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_min]

# 4. Filtro por ocupación
if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = df['ocupacion'].dropna().unique().tolist()
    seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(seleccionadas)]

# 5. Filtro por tipo de vivienda NO Propia
if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[df_filtrado['tipo_vivienda'] != 'Propia']

# 6. Filtro por nombre contiene texto
if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingresa parte del nombre")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

# 7. Filtro por año de nacimiento
if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    año = st.sidebar.selectbox("Selecciona el año", list(range(1949, 2010)))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año]

# 8. Filtro por acceso a internet
if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == (acceso == "Sí")]

# 9. Filtro por ingresos nulos
if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]



# Mostrar resultados
st.subheader("Resultados del filtro")
st.write(f"Total de registros encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)
