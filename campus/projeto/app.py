import streamlit as st
import pandas as pd
import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

# Carregar dados
df = pd.read_csv("dados.csv")

# Título da página
st.title("📍 Mapa de Calor - Cidade Segura")

# Lista de categorias com nomes atualizados
categorias = [
    'Desordem Social',
    'Iluminação Pública',
    'Vias e Calçadas',
    'Lixo e Entulho',
    'Sinalização e Trânsito'
]
opcoes = ['Todos'] + categorias

# Dropdown
categoria = st.selectbox("Escolha a categoria:", opcoes)

# Checkbox para mostrar ou não os marcadores com tags
mostrar_detalhes = st.checkbox("Mostrar marcadores com tags", value=False)

# Calcular coluna de valor com base na opção
if categoria == 'Todos':
    df['valor'] = df[categorias].sum(axis=1)
    df['valor'] = df['valor'] / df['valor'].max()
else:
    df['valor'] = df[categoria] / df[categoria].max()

# Criar o mapa
latitude_central = df['lat'].mean()
longitude_central = df['lon'].mean()
mapa = folium.Map(location=[latitude_central, longitude_central], zoom_start=14)

# Adicionar o mapa de calor
heat_data = [[row['lat'], row['lon'], row['valor']] for _, row in df.iterrows()]
HeatMap(
    heat_data,
    radius=30,
    blur=20,
    max_opacity=0.5,
    min_opacity=0.2
).add_to(mapa)

# Adicionar marcadores com popup se marcado
if mostrar_detalhes:
    for _, row in df[df['valor'] > 0.6].iterrows():
        problemas_dict = {
            '🚓 Desordem Social': row['Desordem Social'],
            '💡 Iluminação Pública': row['Iluminação Pública'],
            '🕳️ Vias e Calçadas': row['Vias e Calçadas'],
            '🗑️ Lixo e Entulho': row['Lixo e Entulho'],
            '🚦 Sinalização e Trânsito': row['Sinalização e Trânsito']
        }

        principais = sorted(problemas_dict.items(), key=lambda x: x[1], reverse=True)[:2]
        principais_problemas = [f"<li>{nome}</li>" for nome, valor in principais if valor > 0]

        popup_html = f"""
        <div style="font-family:sans-serif; font-size:13px; max-width:250px">
            <b style="color:#000000;">Principais relatos</b>
            <ul style="margin: 4px 0; padding-left: 18px;">
                {''.join(principais_problemas)}
            </ul>
        </div>
        """

        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=folium.Popup(folium.IFrame(html=popup_html, width=180, height=80)),
            icon=folium.Icon(icon="info-sign", color="blue", prefix="glyphicon")
        ).add_to(mapa)

# Exibir o mapa no Streamlit
st_folium(mapa, width=700, height=500)
