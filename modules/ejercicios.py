import streamlit as st

from exercises.ejercicio_1 import mostrar_ejercicio_1
from exercises.ejercicio_2 import mostrar_ejercicio_2
from exercises.ejercicio_3 import mostrar_ejercicio_3


def mostrar_ejercicios():

    st.markdown(
        """
        <div class="page-title">
            Ejercicios
        </div>

        <div class="page-description">
            Selecciona uno de los ejercicios disponibles.
        </div>
        """,
        unsafe_allow_html=True
    )

    tab1, tab2, tab3 = st.tabs(
        [
            "🧪 Ejercicio 1",
            "🧪 Ejercicio 2",
            "🧪 Ejercicio 3"
        ]
    )

    with tab1:
        mostrar_ejercicio_1()

    with tab2:
        mostrar_ejercicio_2()

    with tab3:
        mostrar_ejercicio_3()