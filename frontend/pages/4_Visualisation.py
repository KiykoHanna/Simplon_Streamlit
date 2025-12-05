import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

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
    st.write("Graphique avec Matplotlib ")
    fig, ax = plt.subplots()
    ax.plot(df["NA_Sales"])
    st.pyplot(fig)

with tab2:
    st.write("Bar plot avec Plotly")
    fig = px.bar(df[["Name","JP_Sales"]].head(30), x="Name", y="JP_Sales")
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.write("Histogramme avec Seaborn")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.histplot(data=df.head(15), x= "Name", y="EU_Sales", bins=30, ax=ax)
    plt.xticks(rotation=90)
    st.pyplot(fig)

with tab4:
    st.write("kdeplot avec Seaborn")
    fig, ax = plt.subplots(figsize=(6,4))
    sns.kdeplot(data=df, fill=True, x='Other_Sales')
    plt.xticks(rotation=90)
    st.pyplot(fig)

