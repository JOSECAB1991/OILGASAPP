#Módulo
import streamlit as st

from modules.home import mostrar_home
from modules.ejercicios import mostrar_ejercicios


# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="OilGasApp",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# ESTILOS
# ============================================================

st.markdown(
    """
    <style>

    /* --------------------------------------------------------
       VARIABLES VISUALES
    -------------------------------------------------------- */

    :root {
        --oil-dark: #10251d;
        --oil-green: #174c3b;
        --oil-green-light: #28745a;
        --oil-accent: #c69c3c;
        --oil-bg: #f4f7f5;
        --oil-card: #ffffff;
        --oil-text: #1c2923;
        --oil-muted: #6c7972;
    }


    /* --------------------------------------------------------
       FONDO PRINCIPAL
    -------------------------------------------------------- */

    .stApp {
        background-color: var(--oil-bg);
    }


    /* --------------------------------------------------------
       SIDEBAR
    -------------------------------------------------------- */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #10251d 0%,
            #153b2e 55%,
            #174c3b 100%
        );
    }

    section[data-testid="stSidebar"] * {
        color: #ffffff;
    }


    /* --------------------------------------------------------
       LOGOTIPO
    -------------------------------------------------------- */

    .oilgas-logo {
        text-align: center;
        padding: 20px 10px 30px 10px;
    }

    .oilgas-icon {
        font-size: 42px;
    }

    .oilgas-title {
        font-size: 25px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-top: 5px;
    }

    .oilgas-subtitle {
        font-size: 12px;
        color: #b9d0c5 !important;
        margin-top: 3px;
    }


    /* --------------------------------------------------------
       ENCABEZADOS
    -------------------------------------------------------- */

    .page-title {
        font-size: 34px;
        font-weight: 800;
        color: var(--oil-dark);
        margin-bottom: 5px;
    }

    .page-description {
        color: var(--oil-muted);
        font-size: 16px;
        margin-bottom: 25px;
    }


    /* --------------------------------------------------------
       TARJETAS
    -------------------------------------------------------- */

    .info-card {
        background: var(--oil-card);
        border-radius: 14px;
        padding: 25px;
        border: 1px solid #e1e8e4;
        box-shadow: 0 5px 18px rgba(16, 37, 29, 0.06);
        margin-bottom: 20px;
    }

    .info-card h3 {
        color: var(--oil-green);
        margin-top: 0;
    }

    .info-card p {
        color: var(--oil-text);
    }


    /* --------------------------------------------------------
       BADGES
    -------------------------------------------------------- */

    .badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 20px;
        background: #e4f0eb;
        color: var(--oil-green);
        font-size: 13px;
        font-weight: 600;
    }


    /* --------------------------------------------------------
       FOOTER
    -------------------------------------------------------- */

    .footer {
        text-align: center;
        color: #829088;
        font-size: 12px;
        padding: 30px 0 10px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        """
        <div class="oilgas-logo">
            <div class="oilgas-icon">🛢️</div>
            <div class="oilgas-title">OilGasApp</div>
            <div class="oilgas-subtitle">
                Petroleum & Environmental Education
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    pagina = st.radio(
        "NAVEGACIÓN",
        ["🏠 Home", "🧪 Ejercicios"],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            font-size:12px;
            color:#aac1b6;
            padding:10px;
        ">
            OilGasApp<br>
            Plataforma educativa
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ROUTER PRINCIPAL
# ============================================================

if pagina == "🏠 Home":

    mostrar_home()

elif pagina == "🧪 Ejercicios":

    mostrar_ejercicios()
