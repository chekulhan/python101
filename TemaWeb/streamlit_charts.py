import streamlit as st

temperatures = {
    'Monday': 20.85,
    'Tuesday': -5.93,
    'Wednesday': -8.62,
    'Thursday': 30.94,
    'Friday': -8.52,
    'Saturday': 31.17,
    'Sunday': 7.40
}

with st.expander("¿Quieres ver la temperatura de esta semana?"):
    st.bar_chart(temperatures, y_label="Celcius")
