import streamlit as st
from datetime import datetime


if 'incidencias' not in st.session_state:
    st.session_state.incidencias = []


with st.form(key="Incidencias"):
    nombre = st.text_input("¿Quien eres?")
    problema = st.text_input("Describir tu problema")
    submit_buton = st.form_submit_button("Agregar")

    if submit_buton:
        if nombre and problema:
            tiempo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            incidencia = {"hora": tiempo, "nombre": nombre, "problema": problema}
            st.session_state.incidencias.append(incidencia)
            st.success("Tu incidencia ha sido agregado")

if st.button("Mostrar Incidencias"):
    st.write("Listado de incidencias")
    for i in st.session_state.incidencias:
        st.write(i)
