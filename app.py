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
    st.markdown("<h2 style='text-align: left;'>Objetivo General: </h2>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: justify;">
        Identificar el comportamiento de la generación eléctrica de siete diferentes fuentes de energía en Colombia para el periodo 2006-2023.
    </div>
    """, unsafe_allow_html=True)

    imagen5 = Image.open("Media/col.jpg")
    st.image(imagen5, use_container_width=False, width=900,
             caption="León Bello - Edwin Duqeu - Nicólas Duque - Dayan Gaviria"
             )