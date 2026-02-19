import streamlit as st
import pandas as pd

# Expandir os dados com uma coluna lojas (3 lojas diferentes)

# Permitir que a pessoa digite o nome da loja desejado e exiba na tabela somente os meses que tem vendas da loja escolhida

dados = {
    "meses": ["Janeiro", "Fevereiro", "Março", "Abril" , "Maio", "Junho"],
    "vendas": [3000, 3500 , 4000 , 1200, 1600, 3500]
}

df = pd.DataFrame(dados)

st.title("Primeira Tabela Streamlit")
st.divider()

st.dataframe(df)
