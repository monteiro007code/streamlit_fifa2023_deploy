import webbrowser
from datetime import datetime

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

btn = st.button("Acesse os dados no Kaggle")
if btn:
    webbrowser.open_new_tab(
        "https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset"
    )
