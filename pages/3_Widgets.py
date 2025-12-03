import streamlit as st
import pandas as pd

path_csv = r"D:\Programmation\Formation_Simplon\BRIEF_2\app\data\vgsales.csv"
df = pd.read_csv(path_csv, index_col=0)

st.title("Widgets interactifs")
with st.expander("Tache"):
    st.markdown("""
                - Créer un bouton (st.button()).
                - Créer une case à cocher (st.checkbox()).
                - Créer un champ de saisie de texte (st.text_input()).
                - Créer un sélecteur déroulant (st.selectbox()).
                - Créer un curseur (st.slider()).
                """)

buttton = st.button("button")
if buttton:
    
    st.success("Il marche!")

if st.checkbox("Afficher/Masquer le base de donne"):
    st.dataframe(df.head(5))
    st.success("Il marche!")

# Champ
with st.form("Champ pour ramplir"):
    text = st.text_input("Text input")
    age = st.number_input("Number input")

    submitted = st.form_submit_button("Ajouter")

if submitted:
    st.success("Il marche")

column_nb = st.selectbox("Select columns de database", ["NA_Sales", "JP_Sales", "EU_Sales", "Other_Sales"])
min_val = float(df[column_nb].min())
max_val = float(df[column_nb].max())

level_min, level_max = st.slider(column_nb,
                                min_value=min_val,
                                max_value=max_val,
                                value=(min_val, max_val)
                                  )
