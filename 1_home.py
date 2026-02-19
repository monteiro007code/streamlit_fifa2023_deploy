import webbrowser
from datetime import datetime
import openai
import pandas as pd
import streamlit as st


if "data" not in st.session_state:
    df_data = pd.read_csv(
        "datasets/CLEAN_FIFA23_official_data.csv",
        index_col=0,
        skipinitialspace=True,
    )
    df_data.columns = df_data.columns.str.strip().str.replace("Â£", "£", regex=False)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.markdown("# FIFA23 OFICIAL DATASET! ⚽️")
st.sidebar.markdown("Desenvovido por [Asimov Academy](https://www.asimov.academy/)")

btn = st.link_button(
    "Acesse os dados no Kaggle",
    "https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset"
)

st.markdown("""
Este é um projeto de análise de dados utilizando o dataset oficial do FIFA 23. 
O objetivo é explorar e analisar os dados dos jogadores para obter insights sobre suas características, 
desempenho e valor de mercado. O dataset contém informações detalhadas sobre os jogadores, incluindo atributos físicos, 
habilidades técnicas, estatísticas de desempenho e muito mais.""")

