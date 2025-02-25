import pandas as pd
import streamlit as st
from PIL import Image
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np


def generarMenu():
    with st.sidebar:
        col1, col2 = st.columns(2)
        with col1:
            imagen1 = Image.open("Media\ladron.jpeg")
            st.image(imagen1, use_container_width=False, width=800)
        with col2:
            st.header('Ladrón Dimayor Liga Bet Play 2024')
            ##imagen2 = Image.open("Media\ladron.jpeg")
            ##st.image(imagen2, use_container_width=False, width=800)
        ''' with col3:
            imagen3 = Image.open("Media\dimayor.jpg")
            st.image(imagen3)
        with col4:
            imagen4 = Image.open("Media\dimayor.jpg")
            st.image(imagen4)'''
        st.page_link('app.py', label='Home', icon='🏠')
        st.page_link('Pages\informe.py', label='Informe', icon='💯')

def visualizardata(df,titulo):
    data_col = df[df['country'] == 'Colombia']
    # selecciono solo la columna de year y las de share_elec
    data_col1 = data_col.filter(regex="year|share", axis=1)
    data_col1 = data_col1[data_col1["year"] >= 2006]
    data_col1 = data_col1.drop(columns=['nuclear_share_elec'])
    data_col1.columns
    #Coniguramos la visualización
    df2 = pd.DataFrame(df)
    col1, col2, col3 = st.columns([0.5,5,0.5],
                                vertical_alignment='top',
                                )
    with col2:
        '''df2.set_index('Local',inplace=True)
        st.markdown(titulo)   
        st.write(df, unsafe_allow_html=False)
        st.markdown('gráfico de barras')
        sns.set_style('whitegrid')
        total = df2.groupby('Local')[['Goles Local',
                                    'Goles Visitante']].sum()
        goles = pd.DataFrame(total)
        goles['Goles Total'] = goles['Goles Local'] + goles['Goles Visitante']
        goles = goles.reset_index()
        resultado = goles.groupby(['Local']).sum()
        resultado.plot(kind='bar', figsize=(10,10))
        plt.tight_layout()
        st.pyplot(plt)'''
        plt.style.use('dark_background')
        sns.set_palette("bright")  # Colores vibrantes

        # Crear la figura y el eje
        fig, ax = plt.subplots(figsize=(12, 6))

        # Dibujar cada línea
        for col in data_col1.columns[1:]:  # Excluir el año
            ax.plot(data_col1['year'], data_col1[col], label=col.replace("_share_elec", "").capitalize(), linewidth=2)

        # Personalización del gráfico
        ax.set_facecolor("#030764")  # Fondo de la grafica
        ax.grid(color='gray', linestyle='dashdot', linewidth=0.4)  # Rejilla sutil
        ax.set_title("Evolución del Mix Energético en Colombia", fontsize=14, fontweight='bold', color='white')
        ax.set_xlabel("Año", fontsize=12, color='white')
        ax.set_ylabel("Porcentaje de Energía", fontsize=12, color='white')
        ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=12, frameon=True)
        ax.tick_params(axis='both', colors='white')  # Color de los números en ejes
        ax.set_xticks(np.arange(data_col1['year'].min(), data_col1['year'].max() + 1, 1))  # Configurar la grilla para que aparezca cada año
        ax.set_xticklabels([str(year) if year % 1 == 0 else "" for year in data_col1['year']], rotation=0)  # Configurar etiquetas
        ax.set_yticks(np.arange(0, 100, 10))  # Configurar la grilla para que aparezca
        ax.set_yticklabels([str(y) if y % 20 == 0 else "" for y in (np.arange(0, 100, 10))], rotation=0)  # Configurar etiquetas


        # Mostrar gráfico
        st.pyplot(plt)

        data_col2 = data_col.filter(regex="year|electricity", axis=1)
        data_col2 = data_col2[data_col2["year"] >= 2006]
        data_col2.columns
        # Filtrar columnas que contienen 'electricity'
        cols = [col for col in data_col2.columns if 'electricity' in col]

        # Agrupar por 'year' y sumar, reemplazando NaN por 0
        df_grouped = data_col2.groupby('year')[cols].sum()

        #st.write(df_grouped)

        # Sumar todas las columnas de electricidad por año
        total_per_year = df_grouped.sum(axis=1)

        # Graficar en un solo pie chart
        plt.figure(figsize=(8, 8))
        total_per_year.plot(kind='pie', autopct='%1.1f%%', cmap="viridis")

        # Configuración del gráfico
        plt.title('Distribución total de electricidad por año')
        plt.ylabel('')  # Ocultar etiqueta del eje Y

        st.pyplot(plt)

        total_per_year2 = df_grouped.sum(axis=0)

        # Graficar en un solo pie chart
        plt.figure(figsize=(8, 8))
        total_per_year2.plot(kind='pie', autopct='%1.1f%%', cmap="viridis")
        st.pyplot(plt)

        plt.style.use('dark_background')
        sns.set_palette("bright")  # Colores vibrantes

        # Crear la figura y el eje
        fig, ax = plt.subplots(figsize=(12, 6))

        # Dibujar cada línea
        for col in data_col2.columns[1:]:  # Excluir el año
            ax.plot(data_col2['year'], data_col2[col], label=col.replace("_electricity", "").capitalize(), linewidth=2)

        # Personalización del gráfico
        ax.set_facecolor("#030764")  # Fondo de la grafica
        ax.grid(color='gray', linestyle='dashdot', linewidth=0.4)  # Rejilla sutil
        ax.set_title("Evolución del Mix Energético en Colombia", fontsize=14, fontweight='bold', color='white')
        ax.set_xlabel("Año", fontsize=12, color='white')
        ax.set_ylabel("Porcentaje de Energía", fontsize=12, color='white')
        ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=12, frameon=True)
        ax.tick_params(axis='both', colors='white')  # Color de los números en ejes
        ax.set_xticks(np.arange(data_col2['year'].min(), data_col2['year'].max() + 1, 1))  # Configurar la grilla para que aparezca cada año
        ax.set_xticklabels([str(year) if year % 1 == 0 else "" for year in data_col2['year']], rotation=0)  # Configurar etiquetas
        ax.set_yticks(np.arange(0, 100, 10))  # Configurar la grilla para que aparezca
        ax.set_yticklabels([str(y) if y % 20 == 0 else "" for y in (np.arange(0, 100, 10))], rotation=0)  # Configurar etiquetas
         # Mostrar gráfico
        st.pyplot(plt)

        st.write(col)
