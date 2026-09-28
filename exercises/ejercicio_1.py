import streamlit as st

def render_ejercicio_1():

    # ================ ENCABEZADO ===========================
    st.html("""
        <div class="exercise-header">
            <div class="exercise-header-title"> Ejercicio 1 · Producción </div>

            <div class="exercise-header-description"> Cálculo de producción mediante una IPR compuesta
                considerando el punto de presión de burbuja. </div>
        </div>
    """)

    # =============== COLUMNAS ============================
    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )

    # ================ DATOS DE ENTRADA ====================
    with col1:
        st.html("""
            <div class="exercise-card">
                <div class="exercise-card-title">
                    <div class="exercise-card-title-icon"> 📥 </div>
                    Datos de entrada
                </div>
            </div>
        """)

        pr = st.number_input(
            "Presión Promedio Reservorio (psi)",
            min_value=0.0,
            #value=3000.0,
            key="ipr_pr"
        )

        pb = st.number_input(
            "Presión de Burbuja (psi)",
            min_value=0.0,
            #value=2000.0,
            key="ipr_pb"
        )

        j = st.number_input(
            "Índice de Productividad J (bbl/d/psi)",
            min_value=0.0,
            #value=1.5,
            key="ipr_j"
        )

        pwf = st.number_input(
            "Presión de Fondo Fluyente Pwf (psi)",
            min_value=0.0,
            #value=1500.0,
            key="ipr_pwf"
        )

        calcular_prod = st.button(
            "⚡ CALCULAR PRODUCCIÓN",
            key="btn_prod",
            use_container_width=True
        )

    # ============== RESULTADOS =============================
    with col2:
        st.html("""
            <div class="exercise-card">
                <div class="exercise-card-title">
                    <div class="exercise-card-title-icon"> 📊 </div>
                    Resultados
                </div>
            </div>
        """)
        if calcular_prod:
            errores = []

            # --------------- VALIDACIONES --------------------            
            if pr <= 0:
                errores.append("La presión promedio del reservorio debe ser mayor que 0 psi.")
            if pb <= 0:
                errores.append("La presión de burbuja debe ser mayor que 0 psi.")
            if j <= 0:
                errores.append("El índice de productividad J debe ser mayor que 0.")
            if pwf < 0:
                errores.append("La presión de fondo fluyente no puede ser negativa.")
            if pwf > pr:
                errores.append(
                    "La presión de fondo fluyente no puede ser mayor "
                    "que la presión promedio del reservorio."
                )
            
            # ---------- MOSTRAR VALIDACIONES ----------------
            if errores:
                st.error("⚠️ Revisa los siguientes datos antes de calcular:")
                for error in errores:
                    st.write(f"• {error}")
            else:
                # -------------- LÓGICA IPR ---------------------
                qb = (
                    j * (pr - pb)
                    if pr > pb
                    else 0
                )

                qmax = (
                    qb +
                    (j * pb / 1.8)
                )

                if pwf >= pb:
                    q = j * (pr - pwf)
                else:

                    q = (
                        qb +
                        (j * pb / 1.8) *
                        (
                            1
                            - 0.2 * (pwf / pb)
                            - 0.8 * (pwf / pb) ** 2
                        )
                    )

                # ------------- RESULTADOS HTML ------------------
                st.html(f"""
                    <div class="result-box">
                        <div class="result-primary">
                            <div class="result-label"> Caudal de petróleo </div>
                            <div class="result-value"> {q:.2f} bbl/d </div>
                        </div>

                        <div class="result-row">
                            <div class="result-label"> Caudal a la presión de burbuja </div>
                            <div class="result-value"> {qb:.2f} bbl/d </div>
                        </div>

                        <div class="result-row">
                            <div class="result-label"> Caudal máximo teórico </div>
                            <div class="result-value"> {qmax:.2f} bbl/d </div>
                        </div>
                    </div>
                """)