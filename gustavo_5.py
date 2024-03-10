import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MiniMap, MarkerCluster

# Título do aplicativo
st.title("Aplicativo de Mapa com Streamlit")

# Input de latitude e longitude
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")

# Inicializando um DataFrame para armazenar a última coordenada
df = pd.DataFrame(columns=['Latitude', 'Longitude'])

# Botão para adicionar coordenadas
if st.button('Adicionar Coordenada'):
    # Atualizando o DataFrame para manter apenas a última coordenada
    df = pd.DataFrame({'Latitude': [latitude], 'Longitude': [longitude]})
    st.success(f"Coordenada adicionada: Latitude {latitude}, Longitude {longitude}")

# Criando o mapa com zoom no último marcador adicionado
if not df.empty:
    m = folium.Map(location=[df.iloc[-1]['Latitude'], df.iloc[-1]['Longitude']], zoom_start=12)
else:
    m = folium.Map(location=[0, 0], zoom_start=2)

# Adicionando um minimap
minimap = MiniMap()
m.add_child(minimap)

# Adicionando a última coordenada ao mapa
if not df.empty:
    folium.Marker([df.iloc[-1]['Latitude'], df.iloc[-1]['Longitude']]).add_to(m)

# Exibindo o mapa
folium_static(m)
