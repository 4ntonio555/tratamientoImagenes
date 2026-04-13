import streamlit as st
import numpy as np

st.title("Resultados")

if "imagen_original_np" not in st.session_state:
    st.warning("Primero sube una imagen en la página **Cargar imagen**.")
    st.stop()

if "imagen_resultado" not in st.session_state:
    st.warning("Primero procesa la imagen en la página **Procesar**.")
    st.stop()

img_original = st.session_state["imagen_original_np"]
img_resultado = st.session_state["imagen_resultado"]
operacion    = st.session_state.get("operacion_usada", "Desconocida")

# Comparación lado a lado
col1, col2 = st.columns(2)

with col1:
    st.subheader("Imagen original")
    st.image(img_original, use_container_width=True)

with col2:
    st.subheader(f"Resultado — {operacion}")
    st.image(img_resultado, use_container_width=True)

# Métricas
st.divider()
st.subheader("Información de la imagen")

col_a, col_b, col_c = st.columns(3)

h_orig, w_orig = img_original.shape[:2]
h_res,  w_res  = img_resultado.shape[:2]
canales = img_original.shape[2] if img_original.ndim == 3 else 1

col_a.metric("Dimensiones originales", f"{w_orig} × {h_orig} px")
col_b.metric("Dimensiones resultado",  f"{w_res} × {h_res} px")
col_c.metric("Canales originales", canales)
