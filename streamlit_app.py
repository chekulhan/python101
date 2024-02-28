
import streamlit as st

st.title("Mi primer proyecto")
st.write("Hola")
st.markdown("# Hello")
st.markdown("*Hello*")


animales = ("dog", "cat", "bird")
name = st.text_input('Introducir un animal')
if name in animales:
    st.write(f"El animal {name} exist")
else:
    if name:
        st.write(f"El no animal {name} exist")


def aplicarEdad(x):
    return x * 10

edad = st.number_input('¿Qué edad tienes?')

if st.button("Click Me"):
    st.write(f"Tu edad es {aplicarEdad(edad)}")

def calcular(x, y, op):
    if op == "Sumar":
        return x+y
    elif op =="Multiplicar":
        return x*y
    else: return "No existe este opcion."


st.markdown("# Calculadora")
num1 = st.number_input("Introducir el primer número",  
            min_value=0, max_value=100)
num2 = st.number_input("Introducir el segundo número",
            min_value=0, max_value=100)

oper = st.radio("Seleccionar una operación:", ["Sumar", "Multiplicar"])

if st.button("Calcular"): # , on_click=calcular(num1, num2, oper))
    st.markdown(f"# {calcular(num1, num2, oper)}")
    

left_column, right_column = st.columns(2)

with left_column:
    st.markdown("# Hola left")
    st.video("https://www.youtube.com/watch?v=jhoNnICV9Nc")

with right_column:
    st.markdown("# Hola right")


add_slider = st.sidebar.slider('Select a range of values',
       0.0, 100.0, (25.0, 75.0)
)

lenguajes = ("Java", "C#", "Python")
opcion = st.sidebar.selectbox("Seleccionar un lenguaje", lenguajes)

if opcion:
    st.write(f"Has seleccionado :v: {opcion}")


if "counter" not in st.session_state:
    st.session_state.counter=0

if st.button("Contar"):
    st.session_state.counter +=1

st.write(f"{st.session_state.counter} veces que pinchamos")

# streamlit run streamlit_app.py


# -------------------------------------------------------------
# Soporte técnico - sin formulario

import streamlit as st
from datetime import datetime

st.title("Soporte técnico")

with st.form("my_form", clear_on_submit=True):

    nombre = st.text_input('Introducir tu nombre')
    problema = st.text_area('Describir tu problema')

    if st.form_submit_button("Agregar problema"):
        descripcion = nombre + " - " + problema + " - " + str(datetime.now()) 
        with open("problemas.txt", "a") as f:
            f.write(descripcion + "\n")
        
        st.write(f"{nombre}")

if st.button("Generar Informe"):
    with open("problemas.txt", "r") as f:
        st.write(f.readlines())

# Soporte técnico - con formulario -----------------
import streamlit as st
from datetime import date
from datetime import datetime

st.markdown ("### Hello, if you have any problem, please fill out the form below:")

with st.form("my_form", clear_on_submit=True):
    nombre = st.text_input("Nombre del usuario")
    descripcion_problema = st.text_area("Descripción del problema")
    submitted = st.form_submit_button("Agregar problema")
    today = date.today()
    

    if submitted:
        st.write(f"Gracias {nombre}.")
        with open ("problemas1.txt", "a") as archivo:
            archivo.write(f"Nombre: {nombre} -   {descripcion_problema} -  {today}\n")


