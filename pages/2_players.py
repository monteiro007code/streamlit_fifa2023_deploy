import base64
import streamlit as st
import requests
from PIL import Image
from io import BytesIO

@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()


st.set_page_config(page_title="Players", page_icon="⚽", layout="wide")

df_data = st.session_state["data"]

clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)

df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()
player = st.sidebar.selectbox("Jogador", players)

player_estats = df_players[df_players["Name"] == player].iloc[0]


st.image(load_image_64(player_estats["Photo"]))


st.title(player_estats["Name"])
st.markdown(f"**Clube:** {player_estats['Club']}")
st.markdown(f"**Posição:** {player_estats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_estats['Age']}")
col2.markdown(f"**Altura:** {player_estats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_estats['Weight(lbs.)'] * 0.453:.2f}")
st.divider() # Adiciona um divisor para separar as seções

st.subheader(f"Overall: {player_estats['Overall']}")
st.progress(int(player_estats['Overall'])) # Exibe a barra de progresso com base no valor do Overall

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_estats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_estats['Wage(£)']:,}")
col3.metric(label="Cláusula de rescisão", value=player_estats['Release Clause(£)'])
