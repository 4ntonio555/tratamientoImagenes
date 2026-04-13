import streamlit as st
import numpy as np
import cv2

st.title("Procesar imagen")

if "imagen_original_bgr" not in st.session_state:
    st.warning("Primero sube una imagen en la página **Cargar imagen**.")
    st.stop()

img_bgr = st.session_state["imagen_original_bgr"]
img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

# Panel lateral con los controles
with st.sidebar:
    st.header("Configuración")
    operacion = st.selectbox(
        "Operación",
        ["Escala de grises", "Canny (bordes)", "Blur (desenfoque)", "Umbral (threshold)"]
    )

    if operacion == "Canny (bordes)":
        umbral1 = st.slider("Umbral inferior", 0, 255, 100)
        umbral2 = st.slider("Umbral superior", 0, 255, 200)
    elif operacion == "Blur (desenfoque)":
        ksize = st.slider("Tamaño del kernel (impar)", 1, 31, 5, step=2)
    elif operacion == "Umbral (threshold)":
        umbral = st.slider("Umbral", 0, 255, 127)

# Procesar según la operación seleccionada
with st.spinner("Procesando imagen..."):
    if operacion == "Escala de grises":
        resultado = img_gris

    elif operacion == "Canny (bordes)":
        resultado = cv2.Canny(img_gris, umbral1, umbral2)

    elif operacion == "Blur (desenfoque)":
        resultado = cv2.GaussianBlur(img_gris, (ksize, ksize), 0)

    elif operacion == "Umbral (threshold)":
        _, resultado = cv2.threshold(img_gris, umbral, 255, cv2.THRESH_BINARY)

# Guardar resultado en session_state
st.session_state["imagen_resultado"] = resultado
st.session_state["operacion_usada"]  = operacion

st.success(f"Operación aplicada: **{operacion}**")
st.image(resultado, caption=f"Resultado — {operacion}", use_container_width=True)

with st.expander("Ver código de la operación"):
    if operacion == "Escala de grises":
        st.code("img_gris = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)", language="python")
    elif operacion == "Canny (bordes)":
        st.code(f"bordes = cv2.Canny(img_gris, {umbral1}, {umbral2})", language="python")
    elif operacion == "Blur (desenfoque)":
        st.code(f"blur = cv2.GaussianBlur(img_gris, ({ksize}, {ksize}), 0)", language="python")
    elif operacion == "Umbral (threshold)":
        st.code(f"_, resultado = cv2.threshold(img_gris, {umbral}, 255, cv2.THRESH_BINARY)", language="python")
