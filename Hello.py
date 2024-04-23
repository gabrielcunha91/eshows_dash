import streamlit as st
from streamlit.logger import get_logger
import pandas as pd
import os
import numpy as np
from datetime import datetime
import mysql.connector
from utils.queries import *
# from workalendar.america import Brazil
# import openpyxl

st.write('Hello world!')

LOGGER = get_logger(__name__)

def mysql_connection():
  mysql_config = st.secrets["mysql"]

  conn = mysql.connector.connect(
        host=mysql_config['host'],
        port=mysql_config['port'],
        database=mysql_config['database'],
        user=mysql_config['username'],
        password=mysql_config['password']
    )    
  return conn

def execute_query(query, conn):
    cursor = conn.cursor()
    cursor.execute(query)

    # Obter nomes das colunas
    column_names = [col[0] for col in cursor.description]
  
    # Obter resultados
    result = cursor.fetchall()
  
    cursor.close()
    return result, column_names

def run():

    ######## Config Pag ##########
    st.set_page_config(
    page_title="Fluxo_Financeiro_FB",
    page_icon="💰",
    )

    def teste():
        result, column_names = execute_query(GET_TESTE, conn)
        df_teste = pd.DataFrame(result, columns=column_names)

        df_teste['Data_Show'] = pd.to_datetime(df_teste['Data_Show'])

        return df_teste
    df_teste = teste()  

    df_teste

if __name__ == "__main__":
    run()
