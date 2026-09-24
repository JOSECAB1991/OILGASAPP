import streamlit as st

# ============================================
# 1. CONFIGURACIÓN GENERAL DE LA PÁGINA
# ============================================
st.set_page_config(
    page_title="Mi aplicación web moderna",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed"   # Ocultamos el sidebar por defecto
)

# ============================================
# 2. ESTILOS CSS PERSONALIZADOS
# ============================================
st.markdown("""
<style>
    /* Ocultar elementos por defecto de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Fondo general */
    .stApp {
        background-color: #F4F6F8;
    }
    
    /* ENCABEZADO */
    .header-container {
        background: linear-gradient(135deg, #1B3A5C 0%, #2C5F8D 100%);
        padding: 1.5rem 2rem;
        border-radius: 10px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .logo-section {
        display: flex;
        align-items: center;
        gap: 1rem;
    }
    
    .logo-icon {
        font-size: 2.5rem;
    }
    
    .app-title {
        color: white;
        font-size: 1.8rem;
        font-weight: 700;
        margin: 0;
    }
    
    .app-subtitle {
        color: #E8EEF2;
        font-size: 0.9rem;
        margin: 0;
    }
    
    /* BOTONES DE NAVEGACIÓN */
    .nav-buttons {
        display: flex;
        gap: 1rem;
    }
    
    /* Estilo para los page_link de Streamlit */
    div[data-testid="stPageLink-NavLink"] {
        min-width: 120px;
    }
    
    div[data-testid="stPageLink-NavLink"] p {
        font-size: 1rem;
        font-weight: 600;
        text-align: center;
    }
    
    /* CONTENIDO PRINCIPAL */
    .main-content {
        background: white;
        padding: 3rem 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        text-align: center;
        min-height: 400px;
    }
    
    .welcome-title {
        color: #1B3A5C;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .welcome-subtitle {
        color: #E8751A;
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 2rem;
    }
    
    .welcome-text {
        color: #2D3436;
        font-size: 1.1rem;
        line-height: 1.8;
        max-width: 800px;
        margin: 0 auto;
    }
    
    /* PIE DE PÁGINA */
    .footer {
        text-align: center;
        margin-top: 2rem;
        padding: 1.5rem;
        background: white;
        border-radius: 10px;
        border-top: 3px solid #E8751A;
    }
    
    .footer .author {
        color: #1B3A5C;
        font-weight: 700;
        font-size: 1.1rem;
        margin: 0;
    }
    
    .footer .info {
        color: #636E72;
        font-size: 0.95rem;
        margin: 0.3rem 0;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# 3. ENCABEZADO CON LOGO Y BOTONES
# ============================================
col_logo, col_nav = st.columns([3, 1])

with col_logo:
    st.markdown("""
    <div class="header-container">
        <div class="logo-section">
            <div class="logo-icon">🛢️</div>
            <div>
                <h1 class="app-title">Mi aplicación web moderna</h1>
                <p class="app-subtitle">http://127.0.0.0</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_nav:
    st.markdown("<br>", unsafe_allow_html=True)  # Espaciado
    st.markdown("##### 🔘 Navegación")
    # Botón Home (página actual, deshabilitado visualmente)
    home_btn = st.page_link("app.py", label="🏠 Home", icon=None)
    # Botón Ejercicios (va a la otra página)
    ejercicios_btn = st.page_link("pages/1_Ejercicios.py", label="📊 Ejercicios", icon=None)

# ============================================
# 4. CONTENIDO PRINCIPAL (HOME)
# ============================================
st.markdown("""
<div class="main-content">
    <h1 class="welcome-title">¡Bienvenido!</h1>
    <p class="welcome-subtitle">Tarea de sistema web de cálculos personalizado para Oil & Gas</p>
    <p class="welcome-text">
        Esta aplicación ha sido desarrollada utilizando <strong>Python, Streamlit, HTML, CSS y JavaScript</strong> 
        como parte del <strong>Bootcamp Data Analytics for Oil & Gas</strong>.<br><br>
        Haz clic en el botón <strong>"📊 Ejercicios"</strong> del encabezado para acceder a los tres módulos 
        de cálculos: <strong>Producción</strong>, <strong>Perforación</strong> y <strong>Reservorios</strong>.
    </p>
</div>
""", unsafe_allow_html=True)

# ============================================
# 5. PIE DE PÁGINA (FOOTER)
# ============================================
st.markdown("""
<div class="footer">
    <p class="author">Cabrera Yaure José R.</p>
    <p class="info">Sistema de cálculos para Oil & Gas</p>
    <p class="info">Bootcamp Data Analytics for Oil & Gas</p>
</div>
""", unsafe_allow_html=True)
