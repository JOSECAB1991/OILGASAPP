import streamlit as st

from modules.home import render_home
from modules.ejercicios import render_ejercicios

# ================ CONFIGURACIÓN ========================
st.set_page_config(
    page_title="OilGasApp",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ================ CARGAR CSS ==========================
def load_css():
    with open(
        "assets/styles.css",
        "r",
        encoding="utf-8"
    ) as file:
        css = file.read()

    st.html(
        f"<style>{css}</style>"
    )

load_css()

# ============= ESTADO ======================
if "pagina" not in st.session_state:
    st.session_state.pagina = "Home"

# ============= SIDEBAR =====================
with st.sidebar:
    st.html("""
        <div class="brand-container">
            <div class="brand-icon"> 🛢️ </div>

            <div>
                <div class="brand-title"> OilGasApp </div>

                <div class="brand-subtitle"> Petroleum & Environment </div>
            </div>
        </div>
    """)

    st.html("""
        <div class="sidebar-separator"></div>
    """)

    st.html("""
        <div class="menu-title">
            MENÚ PRINCIPAL
        </div>
    """)

    if st.button(
        "🏠 Home",
        key="btn_home",
        use_container_width=True
    ):
        st.session_state.pagina = "Home"
        st.rerun()

    if st.button(
        "🔧 Ejercicios",
        key="btn_ejercicios",
        use_container_width=True
    ):
        st.session_state.pagina = "Ejercicios"
        st.rerun()

# ========== CONTENIDO ==================
if st.session_state.pagina == "Home":
    render_home()

elif st.session_state.pagina == "Ejercicios":
    render_ejercicios()