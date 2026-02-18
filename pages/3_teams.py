import base64
import requests
import streamlit as st
from PIL import Image
from io import BytesIO

@st.cache_data
def load_image_64(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    data = requests.get(url, headers=headers).content
    return "data:image/png;base64," + base64.b64encode(data).decode()

@st.cache_data
def preprocess_row(url):
    if isinstance(url, str) and url.startswith("http"):
        return load_image_64(url)
    return url



st.set_page_config(page_title="Players", page_icon="⚽", layout="wide")

df_data = st.session_state["data"]
clubes = df_data["Club"].unique()
club = st.sidebar.selectbox("Clube", clubes)    

df_filtered = df_data[df_data["Club"] == club].set_index("Name")



df_filtered["Photo"] = df_filtered["Photo"].apply(preprocess_row)
df_filtered["Flag"] = df_filtered["Flag"].apply(preprocess_row)
df_filtered["Club Logo"] = df_filtered["Club Logo"].apply(preprocess_row)


st.markdown(f"## {club}")

columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)", "Joined",
           "Height(cm.)","Weight(lbs.)", "Contract Valid Until", "Release Clause(£)"]

st.dataframe(df_filtered[columns],
             column_config={
                 "Overall": st.column_config.ProgressColumn(
                     "Overall", format="%d", min_value=0, max_value=100),

                "Wage(£)": st.column_config.ProgressColumn(
                     "Wage(£)", format="£%d", min_value=0, max_value=df_filtered["Wage(£)"].max()
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),

                
             })