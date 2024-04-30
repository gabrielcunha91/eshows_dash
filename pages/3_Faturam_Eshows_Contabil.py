import streamlit as st
import pandas as pd
import datetime
import calendar


st.set_page_config(
    page_title="Faturam_Eshows_Contabil",
    page_icon="🎵",
    layout="wide"
)

### Puxando Dados ###
df_faturam_fiscal = st.session_state["faturam_fiscal"]


# Filtrando Data
today = datetime.datetime.now()
last_year = today.year - 1
jan_last_year = datetime.datetime(last_year, 1, 1)
last_day_of_month = calendar.monthrange(today.year, today.month)[1]
this_month_this_year = datetime.datetime(today.year, today.month, last_day_of_month)
dec_this_year = datetime.datetime(today.year, 12, 31)
first_day_this_month = datetime.datetime(today.year, today.month, 1)
last_day_of_last_month = first_day_this_month - datetime.timedelta(days=1)
first_day_last_month = datetime.datetime(today.year, today.month - 1, 1) if today.month > 1 else datetime.datetime(today.year - 1, 12, 1)

date_input = st.date_input("Período",
                           (first_day_last_month, last_day_of_last_month),
                           jan_last_year,
                           dec_this_year,
                           format="DD/MM/YYYY"
                           )

# Convertendo as datas de input para datetime
date_input_start = pd.to_datetime(date_input[0])
date_input_end = pd.to_datetime(date_input[1])

mask = (df_faturam_fiscal["Data_Show"] >= date_input_start) & (df_faturam_fiscal["Data_Show"] <= date_input_end)
df_faturam_fiscal_filtrado = df_faturam_fiscal[mask]

df_faturam_fiscal_filtrado


