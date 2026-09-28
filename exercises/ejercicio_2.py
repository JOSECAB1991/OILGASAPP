import streamlit as st


def render_ejercicio_2():
    # =========== ENCABEZADO =================================
    st.html("""
        <div class="exercise-header">
            <div class="exercise-header-title"> Ejercicio 2 · Presión Hidrostática </div>
            <div class="exercise-header-description">
                Determinación de la presión hidrostática generada
                por la columna de lodo durante una operación de perforación.
            </div>
        </div>
    """)

    # ==================== COLUMNAS ===========================
    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )

    # =================== DATOS DE ENTRADA ===================
    with col1:
        st.html("""
            <div class="exercise-card-title">
                <div class="exercise-card-title-icon"> 📥 </div>
                Datos de entrada
            </div>
        """)

        peso_lodo = st.number_input(
            "Peso del lodo (ppg)",
            min_value=0.0,
            #value=10.0,
            step=0.1,
            key="perf_peso_lodo"
        )

        prof_pozo = st.number_input(
            "Profundidad del Pozo (ft)",
            min_value=0.0,
            #value=10000.0,
            step=100.0,
            key="perf_prof_pozo"
        )

        prof_vertical = st.number_input(
            "Profundidad Vertical (ft)",
            min_value=0.0,
            #value=9500.0,
            step=100.0,
            key="perf_prof_vertical"
        )

        pres_ref = st.number_input(
            "Presión de Referencia (psi)",
            min_value=0.0,
            #value=5000.0,
            step=100.0,
            key="perf_pres_ref"
        )

        #st.markdown("<br>", unsafe_allow_html=True)

        calcular_perf = st.button(
            "⚡ CALCULAR PRESIÓN",
            key="btn_perf",
            use_container_width=True
        )

    # ==================== RESULTADOS ========================
    with col2:
        st.html("""
            <div class="exercise-card-title">
                <div class="exercise-card-title-icon"> 📊 </div>
                Resultados
            </div>
        """)
        if calcular_perf:
            errores = []
            if peso_lodo <= 0:
                errores.append("El peso del lodo debe ser mayor que 0 ppg.")
            if prof_pozo <= 0:
                errores.append("La profundidad del pozo debe ser mayor que 0 ft.")
            if prof_vertical <= 0:
                errores.append("La profundidad vertical debe ser mayor que 0 ft.")
            if prof_vertical > prof_pozo:
                errores.append("La profundidad vertical no puede ser mayor que la profundidad del pozo.")
            if pres_ref < 0:
                errores.append("La presión de referencia no puede ser negativa.")
            if errores:
                st.error("⚠️ Corrige los siguientes datos antes de calcular:")
                for error in errores:
                    st.write(f"• {error}")
                st.stop()

            # ---------------- CÁLCULOS ----------------------
            gradiente = 0.052 * peso_lodo
            pres_hidro = (gradiente * prof_vertical)
            diferencial = (pres_hidro - pres_ref)

            # ------------------ RESULTADOS ------------------------------
            st.html(f"""
                <div class="result-box">
                    <div class="result-primary">
                        <div class="result-label"> Presión hidrostática </div>
                        <div class="result-value"> {pres_hidro:.2f} psi </div>
                    </div>
                    <div class="result-row">
                        <div class="result-label"> Gradiente hidrostático </div>
                        <div class="result-value"> {gradiente:.4f} psi/ft </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> Diferencial de presión </div>
                        <div class="result-value"> {diferencial:.2f} psi </div>
                    </div>
                </div>
            """)