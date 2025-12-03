import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

path_csv = r"D:\Programmation\Formation_Simplon\BRIEF_2\app\data\vgsales.csv"
df = pd.read_csv(path_csv, index_col=0)

st.title("Visualisation de données")
with st.expander("Tache"):
    st.markdown("""
                - Créer des graphiques avec Matplotlib (st.pyplot()).
                - Créer des graphiques interactifs avec Plotly (st.plotly_chart()).
                - Créer des graphiques avec Seaborn (st.pyplot() après avoir créé le graphique avec Seaborn).
                """)
    
st.header("Sales")

column_nb = ["NA_Sales", "JP_Sales", "EU_Sales", "Other_Sales"]

tab1, tab2, tab3, tab4 = st.tabs(column_nb)

with tab1:
    fig, ax = plt.subplots()
    ax.plot(df["NA_Sales"])
    st.pyplot(fig)

with tab2:
    fig, ax = plt.subplots()
    ax.plot(df["JP_Sales"])
    st.plotly_chart(fig)

with tab3:
    fig, ax = plt.subplots()
    ax.plot(df["EU_Sales"])
    st.pyplot(fig)

with tab4:
    fig, ax = plt.subplots()
    ax.plot(df["Other_Sales"])
    st.pyplot(fig)

