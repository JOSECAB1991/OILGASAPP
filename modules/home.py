import streamlit as st


def mostrar_home():

    st.markdown(
        """
        <div class="page-title">
            Bienvenido a OilGasApp
        </div>

        <div class="page-description">
            Plataforma educativa para el aprendizaje aplicado
            al sector petrolero, gasífero y ambiental.
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # INFORMACIÓN DEL ESTUDIANTE
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="info-card">

            <h3>👨‍🎓 Información del estudiante</h3>

            <p>
                <b>Nombre:</b> Nombre del estudiante
            </p>

            <p>
                <b>Carrera:</b> Ingeniería / Tecnología
            </p>

            <p>
                <b>Asignatura:</b> Nombre de la asignatura
            </p>

            <p>
                <b>Docente:</b> Nombre del docente
            </p>

            <span class="badge">
                Estudiante
            </span>

        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # INFORMACIÓN DE LA APLICACIÓN
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="info-card">

                <h3>🛢️ Industria</h3>

                <p>
                    Aplicación orientada al análisis y
                    aprendizaje relacionado con la industria
                    petrolera y gasífera.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="info-card">

                <h3>🌱 Medio ambiente</h3>

                <p>
                    Consideración de aspectos ambientales,
                    sostenibilidad y gestión responsable
                    de los recursos.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="info-card">

                <h3>💻 Tecnología</h3>

                <p>
                    Herramientas digitales para resolver
                    problemas y desarrollar ejercicios
                    prácticos.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # INFORMACIÓN GENERAL
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="info-card">

            <h3>📚 Acerca de OilGasApp</h3>

            <p>
                OilGasApp es una plataforma educativa diseñada
                para centralizar diferentes ejercicios,
                simulaciones y herramientas relacionadas con
                el sector Oil & Gas.
            </p>

            <p>
                Utiliza tecnologías web modernas para ofrecer
                una experiencia sencilla, interactiva y
                orientada al aprendizaje práctico.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="footer">
            OilGasApp © 2026 · Plataforma educativa
        </div>
        """,
        unsafe_allow_html=True
    )