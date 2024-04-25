import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Faturam_Eshows_Gerencial",
    page_icon="🎵",
    layout="wide"
)


### Puxando Dados ###
df_view_faturam_eshows = st.session_state["view_faturam_eshows"]

df_view_faturam_eshows
### Filtros ###


### Agrupamentos ###
df_view_faturam_ajustado = df_view_faturam_eshows[["Primeiro_Dia_Mes", "Casa", "Valor_Total"]]

df_view_faturam_por_mes =df_view_faturam_ajustado.groupby("Primeiro_Dia_Mes").agg({"Casa": "nunique", "Valor_Total": "sum"})

df_view_faturam_por_mes



