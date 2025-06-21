import folium
from folium.plugins import HeatMap
import pandas as pd
import numpy as np

# Coordenadas de Brasília (centro aproximado)
latitude = -15.7942
longitude = -47.8822

# Gerar 100 pontos simulados ao redor do centro
np.random.seed(42)
n = 100

df = pd.DataFrame({
    'lat': np.random.normal(loc=latitude, scale=0.01, size=n),
    'lon': np.random.normal(loc=longitude, scale=0.01, size=n),
    'assaltos': np.random.randint(0, 10, size=n),
    'iluminacao': np.random.randint(0, 10, size=n),
    'buracos': np.random.randint(0, 10, size=n),
    'lixo': np.random.randint(0, 10, size=n),
    'semaforos': np.random.randint(0, 10, size=n),
})

# Normalizar cada categoria de 0 a 1
for coluna in ['assaltos', 'iluminacao', 'buracos', 'lixo', 'semaforos']:
    df[f'{coluna}_norm'] = df[coluna] / df[coluna].max()

# Criar o mapa base
mapa = folium.Map(location=[latitude, longitude], zoom_start=14)

def adicionar_camada_calor(df, coluna, nome_camada, mapa):
    heat_data = [[row['lat'], row['lon'], row[coluna]] for _, row in df.iterrows()]
    camada = folium.FeatureGroup(name=nome_camada)
    HeatMap(
        heat_data,
        radius=23,          
        blur=25,            
        max_val=1.0,
        min_opacity=0.5,    
        max_opacity=0.7     
    ).add_to(camada)
    camada.add_to(mapa)


# Adicionar as camadas desejadas
adicionar_camada_calor(df, 'assaltos_norm', 'Assaltos', mapa)
adicionar_camada_calor(df, 'iluminacao_norm', 'Iluminação Ruim', mapa)
adicionar_camada_calor(df, 'buracos_norm', 'Ruas Esburacadas', mapa)
adicionar_camada_calor(df, 'lixo_norm', 'Acúmulo de Lixo', mapa)
adicionar_camada_calor(df, 'semaforos_norm', 'Semáforos com Defeito', mapa)

# Adicionar controle de camadas
folium.LayerControl().add_to(mapa)

# Salvar o mapa final
mapa.save("mapa_calor_df.html")
