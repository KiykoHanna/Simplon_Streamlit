#frontend/pages/0_pages
import streamlit as st
import requests
import os
from dotenv import load_dotenv 

load_dotenv()

API_ROOT_URL =  f"http://127.0.0.1:{os.getenv('FASTAPI_PORT', '8080')}"
               
st.title("Inserer une nouvelle citation ")

with st.form("insert_form"):
    st.text_area("text")
    submitted = st.form_submit_button("Ajout la citation")

    if submitted:
        new_quote_text = st.text_input("new quote")
        data = {"text":new_quote_text}
        st.info("envoi a l'API")

    try:
        response = requests.post(API_ROOT_URL)

        if response:

            if response.status_code == 200:
                result = response.json()
                st.success(f"Citation ajoités")
            else:
                st.error(f"Errore ")

    except:
        st.error("Erreur")