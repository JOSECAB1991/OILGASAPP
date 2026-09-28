import streamlit as st

def render_home():
    # ================= HEADER ===============================
    st.html("""
        <div class="page-header">
            <h1> Bienvenido a OilGasApp </h1>

            <p> Plataforma para el análisis y resolución de ejercicios relacionados
            con la industria petrolera. </p>
        </div>
    """)

    #st.markdown("<br>", unsafe_allow_html=True)

    # ============= INFORMACIÓN DEL ESTUDIANTE ===============
    st.html("""
        <div class="section-title"> Información del estudiante </div>
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.html("""
            <div class="info-card">
                <div class="card-icon"> 👨‍🎓 </div>

                <div class="card-label"> ESTUDIANTE </div>

                <div class="card-value"> Cabrera Yuare José Reinel </div>
            </div>
        """)

    with col2:
        st.html("""
            <div class="info-card">
                <div class="card-icon"> 🎓 </div>

                <div class="card-label"> DESCRIPCIÓN CORTA </div>

                <div class="card-value"> Sistema de cálculo para OIL & GAS </div>
            </div>
        """)

    with col3:
        st.html("""
            <div class="info-card">
                <div class="card-icon"> 📚 </div>

                <div class="card-label"> BOOTCAMP </div>

                <div class="card-value"> Data Analitics for OIL & GAS </div>
            </div>
        """)

    #st.markdown("<br>", unsafe_allow_html=True)