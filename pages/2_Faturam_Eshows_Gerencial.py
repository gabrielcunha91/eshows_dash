import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Faturam_Eshows_Gerencial",
    page_icon="🎵",
    layout="wide"
)


### Puxando Dados ###
df_view_faturam_eshows = st.session_state["view_faturam_eshows"]


### Filtros ###


### Agrupamentos ###
df_view_faturam_ajustado = df_view_faturam_eshows[["Primeiro_Dia_Mes", "p_ID", "Casa", "Valor_Total", "Comissao_Eshows_B2B",
                                                    "Comissao_Eshows_B2C", "SAAS_Mensalidade", "SAAS_Percentual", "Curadoria",
                                                      "Taxa_Adiantamento", "Taxa_Emissao_NF", "Grupo"]]


df_view_faturam_por_mes = df_view_faturam_ajustado.groupby("Primeiro_Dia_Mes").agg(
    {"Casa": "nunique", "p_ID": "nunique", "Valor_Total": "sum", "Comissao_Eshows_B2B": "sum", "Comissao_Eshows_B2C": "sum",
     "SAAS_Mensalidade": "sum", "SAAS_Percentual": "sum", "Curadoria": "sum", "Taxa_Adiantamento": "sum", "Taxa_Emissao_NF": "sum"})

df_view_faturam_por_mes["Perc_Comissao"] = df_view_faturam_por_mes["Comissao_Eshows_B2B"]/df_view_faturam_por_mes["Valor_Total"]
colunas_para_somar_faturam = ["Comissao_Eshows_B2B", "Comissao_Eshows_B2C", "SAAS_Mensalidade", "SAAS_Percentual", "Curadoria",
                              "Taxa_Adiantamento", "Taxa_Emissao_NF"]

df_view_faturam_por_mes["Faturam_Total"] = df_view_faturam_por_mes[colunas_para_somar_faturam].sum(axis=1)


## Faturamento por mes consolidado geral
df_view_faturam_por_mes

# Filtando grupos
grupos = df_view_faturam_ajustado["Grupo"].unique()
grupo = st.selectbox("Grupo", grupos)

df_view_faturam_por_grupo =  df_view_faturam_ajustado[df_view_faturam_ajustado["Grupo"] == grupo]


## Faturamento por mes por grupo
df_view_faturam_por_mes_por_grupo = df_view_faturam_por_grupo.groupby("Primeiro_Dia_Mes").agg(
    {"Casa": "nunique", "p_ID": "nunique", "Valor_Total": "sum", "Comissao_Eshows_B2B": "sum", "Comissao_Eshows_B2C": "sum",
     "SAAS_Mensalidade": "sum", "SAAS_Percentual": "sum", "Curadoria": "sum", "Taxa_Adiantamento": "sum", "Taxa_Emissao_NF": "sum"})


df_view_faturam_por_mes_por_grupo

# ## Abrindo as propostas
# st.markdown("Abertura por propostas:") 
# df_view_faturam_eshows

