import pandas as pd
import utilidades as util
import streamlit as st
from PIL import Image

#Página de index
st.set_page_config(
    page_title="Transición Energética Sobre Datos",
    initial_sidebar_state="collapsed",
    layout="wide",
    page_icon="🌱"
)


#Llamamos la función 
util.generarMenu()

#Estructura de presentación
left_col, center_col, right_col = st.columns([1,8,1],
                                             vertical_alignment="center")


#Edito la center_col
with center_col:
    import streamlit as st

    st.markdown("<h1 style='text-align: center;'>Informe sobre la Transición Energética</h1>", unsafe_allow_html=True)
    st.write("""
En este espacio, VA EL OBJETIVO PRINCIPAL.

             ACÁ DEBERÍAN DE IR LOS DEMÁS OBJETIVOS (SI APLICA).
            """)
    imagen5 = Image.open("Media\col.jpg")
    st.image(imagen5, use_container_width=False, width=900,
             caption="INTEGRANTES DEL EQUIPO"
             )