import streamlit as st
import pandas as pd
import io

path_csv = r"D:\Programmation\Formation_Simplon\BRIEF_2\app\data\vgsales.csv"
df = pd.read_csv(path_csv, index_col=0)


st.title("Base de donne de jouex videos")
with st.expander("Tache"):
    st.markdown("""
                ## Chargement et affichage de données
                    - Charger un jeu de données avec Pandas (pd.read_csv()).
                    - Afficher un DataFrame Pandas (st.dataframe()).
                    - Afficher un tableau statique (st.table()).
                """)
st.dataframe(df.head(10), width="stretch")

st.subheader("Statistic")
st.table(df.describe())

st.subheader("Info")

buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()

st.text(info_str)