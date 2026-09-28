import streamlit as st


def render_ejercicio_3():
    # ============== ENCABEZADO ==============================
    st.html("""
        <div class="exercise-header">
            <div class="exercise-header-title"> Ejercicio 3 · Estimación Volumétrica del POES </div>
            <div class="exercise-header-description">
                Estimación del Petróleo Original en Sitio mediante
                el método volumétrico y cálculo del volumen potencialmente recuperable.
            </div>
        </div>
    """)

    # =============== COLUMNAS ==============================
    col1, col2 = st.columns(
        [1, 1],
        gap="large"
    )

    # ================== DATOS DE ENTRADA ====================
    with col1:
        st.html("""
            <div class="exercise-card-title">
                <div class="exercise-card-title-icon"> 📥 </div>
                Datos de entrada
            </div>
        """)

        # -------- GEOMETRÍA DEL RESERVORIO ----------------
        area = st.number_input(
            "Área del reservorio (acres)",
            min_value=0.0,
            #value=1000.0,
            step=100.0,
            key="res_area"
        )

        esp_bruto = st.number_input(
            "Espesor Bruto (ft)",
            min_value=0.0,
            #value=50.0,
            step=5.0,
            key="res_esp_bruto"
        )

        ntg = st.number_input(
            "Relación Net-to-Gross (fracción)",
            min_value=0.0,
            max_value=1.0,
            #value=0.8,
            step=0.01,
            key="res_ntg"
        )

        # ---------- PROPIEDADES DEL RESERVORIO --------------
        porosidad = st.number_input(
            "Porosidad efectiva (fracción)",
            min_value=0.0,
            max_value=1.0,
            #value=0.2,
            step=0.01,
            key="res_porosidad"
        )

        swi = st.number_input(
            "Saturación Inicial de Agua (fracción)",
            min_value=0.0,
            max_value=1.0,
            #value=0.3,
            step=0.01,
            key="res_swi"
        )

        boi = st.number_input(
            "Factor Volumétrico Inicial de Petróleo (rb/stb)",
            min_value=0.0,
            #value=1.2,
            step=0.01,
            key="res_boi"
        )

        # ----------------- RECUPERACIÓN ---------------------
        f_recobro = st.number_input(
            "Factor de Recobro (fracción)",
            min_value=0.0,
            max_value=1.0,
            #value=0.3,
            step=0.01,
            key="res_f_recobro"
        )

        #st.markdown("<br>", unsafe_allow_html=True)

        calcular_res = st.button(
            "⚡ CALCULAR POES",
            key="btn_res",
            use_container_width=True
        )

    # ==================== RESULTADOS =======================
    with col2:
        st.html("""
            <div class="exercise-card-title">
                <div class="exercise-card-title-icon"> 📊 </div>
                Resultados
            </div>
        """)

        if calcular_res:
            errores = []
            if area <= 0:
                errores.append("El área del reservorio debe ser mayor que 0 acres.")
            if esp_bruto <= 0:
                errores.append("El espesor bruto debe ser mayor que 0 ft.")
            if not 0 < ntg <= 1:
                errores.append("El NTG debe estar entre 0 y 1.")
            if not 0 < porosidad <= 1:
                errores.append("La porosidad debe estar entre 0 y 1.")
            if not 0 <= swi < 1:
                errores.append("La saturación de agua inicial debe estar entre 0 y 1.")
            if boi <= 0:
                errores.append("El factor volumétrico inicial Boi debe ser mayor que 0.")
            if not 0 <= f_recobro <= 1:
                errores.append("El factor de recobro debe estar entre 0 y 1.")
            if errores:
                st.error("⚠️ Corrige los siguientes datos antes de calcular:")
                for error in errores:
                    st.write(f"• {error}")
                st.stop()

            # ------------------ CÁLCULOS --------------------
            esp_neto = (esp_bruto * ntg)
            poes_stb = (7758 * area * esp_neto * porosidad * (1 - swi)) / boi
            poes_mmstb = (poes_stb / 1_000_000)
            vol_rec_stb = (poes_stb * f_recobro)
            vol_rec_mmstb = (vol_rec_stb / 1_000_000)

            # ----------------- RESULTADOS ----------------
            st.html(f"""
                <div class="result-box">
                    <div class="result-primary">
                        <div class="result-label"> POES · Petróleo Original en Sitio </div>
                        <div class="result-value"> {poes_mmstb:.3f} MMSTB </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> Espesor neto </div>
                        <div class="result-value"> {esp_neto:.2f} ft </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> POES en STB </div>
                        <div class="result-value"> {poes_stb:,.0f} STB </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> POES en MMSTB </div>
                        <div class="result-value"> {poes_mmstb:.3f} MMSTB </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> Volumen recuperable </div>
                        <div class="result-value"> {vol_rec_stb:,.0f} STB </div>
                    </div>

                    <div class="result-row">
                        <div class="result-label"> Volumen recuperable </div>
                        <div class="result-value"> {vol_rec_mmstb:.3f} MMSTB </div>
                    </div>
                </div>
            """)