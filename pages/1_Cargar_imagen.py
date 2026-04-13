import streamlit as st
import numpy as np
import cv2
from PIL import Image

st.title("Cargar imagen")
st.write("Sube una imagen en formato JPG o PNG para procesarla.")

archivo = st.file_uploader(
    "Sube una imagen",
    type=["jpg", "jpeg", "png"]
)

if archivo is not None:
    img_pil = Image.open(archivo)
    img_np  = np.array(img_pil)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Guardar en session_state para compartir con las otras páginas
    st.session_state["imagen_original_np"]  = img_np
    st.session_state["imagen_original_bgr"] = img_bgr

    st.success("Imagen cargada correctamente.")
    st.image(img_np, caption="Imagen cargada", use_container_width=True)
else:
    st.info("Sube una imagen para comenzar.")
