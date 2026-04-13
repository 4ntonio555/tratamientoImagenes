import streamlit as st

def inicio():
    st.title("🏠 Página principal")
    st.write("Selecciona una sección en el menú de la izquierda.")

pg = st.navigation([
    st.Page(inicio,                        title="Inicio",        icon="🏠"),
    st.Page("pages/1_Cargar_imagen.py",    title="Cargar imagen", icon="📁"),
    st.Page("pages/2_Procesar.py",         title="Procesar",      icon="⚙️"),
    st.Page("pages/3_Resultados.py",       title="Resultados",    icon="📊"),
])

pg.run()
