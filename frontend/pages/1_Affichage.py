#frontend/pages/1_pages
import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_ROOT_URL =  f"http://127.0.0.1:{os.getenv('FASTAPI_PORT', '8080')}"
API_URL = API_ROOT_URL + "/read"

st.title("Read ALL")

if st.button("Lire toutes les donne"):
    st.info("")


# st.set_page_config(page_title="Affichage de texte")
# st.title("Affichage de text")
# st.header("Points à aborder")

# col_1, col_2 = st.columns(2, width="stretch")
# with col_1:
#     st.markdown("""
#                 1. Installation et configuration
#                     - Installer Streamlit (pip install streamlit).
#                     - Créer un fichier hello.py et faites import streamlit as st
#                     - Lancer une application Streamlit simple (streamlit run hello.py).
#                 2. Affichage de texte
#                     - Afficher un titre (st.title()).
#                     - Afficher des en-têtes (st.header(), st.subheader()).
#                     - Afficher du texte (st.write()).
#                     - Afficher du Markdown (st.markdown()).
#                 3. Chargement et affichage de données
#                     - Charger un jeu de données avec Pandas (pd.read_csv()).
#                     - Afficher un DataFrame Pandas (st.dataframe()).
#                     - Afficher un tableau statique (st.table()).
#                 4. Widgets interactifs
#                     - Créer un bouton (st.button()).
#                     - Créer une case à cocher (st.checkbox()).
#                     - Créer un champ de saisie de texte (st.text_input()).
#                     - Créer un sélecteur déroulant (st.selectbox()).
#                     - Créer un curseur (st.slider()).
#                 """)
# with col_2:
#     st.markdown("""            
#             5. Mise en page
#                 - Utiliser des colonnes (st.columns()).
#                 - Utiliser des conteneurs extensibles (st.expander()).
#                 - Utiliser des onglets (st.tabs())
#             6. Visualisation de données
#                 - Créer des graphiques avec Matplotlib (st.pyplot()).
#                 - Créer des graphiques interactifs avec Plotly (st.plotly_chart()).
#                 - Créer des graphiques avec Seaborn (st.pyplot() après avoir créé le graphique avec Seaborn).
#             """)