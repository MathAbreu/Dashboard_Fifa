# Home.py
import streamlit as st
import pandas as pd
from datetime import datetime
import webbrowser as wb

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"].notna()]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data


st.write("# FIFA 23 DATASET - CESAR School")
st.sidebar.markdown("Desenvolvidor para a pós-gradução da Cesar School")

btn = st.button("Acesse os dados no Kaggle")
if btn:
    wb.open_new_tab("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

integrantes_df = "Grupo composto por: <br> **Matheus Barreto** <br> **Eduardo Leite** <br> **Lucas Niemeyer**"
st.markdown(integrantes_df, unsafe_allow_html= True)
descricao_df = "About Dataset <br> <br> CONTEXT <br> <br> The Football Player Dataset from 2017 to 2023 provides comprehensive information about professional football players. The dataset contains a wide range of attributes, including player demographics, physical characteristics, playing statistics, contract details, and club affiliations. With over 17,000 records, this dataset offers a valuable resource for football analysts, researchers, and enthusiasts interested in exploring various aspects of the footballing world, as it allows for studying player attributes, performance metrics, market valuation, club analysis, player positioning, and player development over time."  
st.markdown(descricao_df, unsafe_allow_html= True)
