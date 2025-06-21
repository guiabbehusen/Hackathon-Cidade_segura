# 🚨 Hackathon - Cidade Segura

Este projeto foi desenvolvido para o Hackathon **Cidade Segura**, com o objetivo de criar uma solução que permita aos cidadãos identificar e relatar problemas urbanos por meio de um **mapa de calor interativo**.

## 📍 Objetivo

Facilitar o mapeamento colaborativo de locais com:

- Desordem social
- Iluminação pública precária
- Problemas em vias e calçadas
- Acúmulo de lixo ou entulho
- Falta de sinalização e problemas de trânsito

A aplicação exibe **mapas interativos com filtragem por categoria** e permite visualizar os **locais mais críticos** com base na intensidade dos relatos.

## 💻 Tecnologias Utilizadas

- [Streamlit](https://streamlit.io/)
- [Folium](https://python-visualization.github.io/folium/)
- [Pandas](https://pandas.pydata.org/)
- [streamlit-folium](https://github.com/randyzwitch/streamlit-folium)

## 🗂️ Estrutura do Projeto

```bash
Hackathon-cidade-segura/
├── campus/
│   └── projeto/
│       ├── app.py            # Script principal com a aplicação Streamlit
│       ├── dados.csv         # Base de dados com localização e categorias
│       └── requirements.txt  # Lista de dependências para rodar o projeto
