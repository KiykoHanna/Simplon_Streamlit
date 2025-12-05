import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# import data
path_csv = r"D:\Programmation\Formation_Simplon\BRIEF_2\app\data\vgsales.csv"
df = pd.read_csv(path_csv, index_col=0)



# Title
st.title("Filtres et interactions")
with st.expander("Tache"):
    st.markdown("""
                - Filtrer les données en fonction des sélections de l'utilisateur. 
                - C’est à dire que par exemple avec un select, checkbox vous proposez quelle colonne à afficher.
                - Afficher des informations détaillées sur un élément sélectionné dans un graphique                
                """)

column_nb = df.select_dtypes(include='number').columns.tolist()
col = st.selectbox("Choisir la colonne pour filtration", column_nb)
col1, col2 = st.columns(2, width="stretch")

min_val = float(df[col].min())
max_val = float(df[col].max())
with col1:
    st.write(f"min = {min_val} _______   max = {max_val}")

    level_min, level_max = st.slider(col,
                                    min_value=min_val,
                                    max_value=max_val,
                                    value=(min_val, max_val)
                                    )

    mask = (level_min <= df[col]) & (df[col] <= level_max)
    st.dataframe(df[mask], height=350)

with col2:
    fig, ax = plt.subplots(figsize=(4, 6))
    sns.histplot(data=df.loc[mask, col], kde=True)
    st.pyplot(fig)