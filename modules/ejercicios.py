import streamlit as st

from exercises.ejercicio_1 import render_ejercicio_1
from exercises.ejercicio_2 import render_ejercicio_2
from exercises.ejercicio_3 import render_ejercicio_3


def render_ejercicios():
    tab1, tab2, tab3 = st.tabs([
        "🛢️ Ejercicio 1 - Producción",
        "🌱 Ejercicio 2 - Perforación",
        "⚙️ Ejercicio 3 - Reservorios"
    ])

    with tab1:
        render_ejercicio_1()

    with tab2:
        render_ejercicio_2()

    with tab3:
        render_ejercicio_3()