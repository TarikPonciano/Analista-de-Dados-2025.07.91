import streamlit as st
import pandas as pd

# Expandir os dados com uma coluna lojas (3 lojas diferentes)

# Permitir que a pessoa digite o nome da loja desejado e exiba na tabela somente os meses que tem vendas da loja escolhida

dados = {
    "meses": ["Janeiro", "Fevereiro", "Março", "Abril" , "Maio", "Junho"],
    "vendas": [3000, 3500 , 4000 , 1200, 1600, 3500],
    "lojas": ["Loja C", "Loja B", "Loja A", "Loja B", "Loja C", "Loja C"]
}

df = pd.DataFrame(dados)

st.title("Primeira Tabela Streamlit")
st.divider()

st.dataframe(df)
st.divider()

st.header("Versão Filtrada por Loja")

#loja = st.text_input("Digite o nome da loja:")

lojas = ["Todos"] + list(df["lojas"].unique())

loja = st.selectbox("Escolha uma loja: ", lojas)

dfLojas = df[df["lojas"]==loja]

if loja == "Todos":
    st.dataframe(df)
else:
    st.dataframe(dfLojas)

# Produzir uma tabela (groupby) que exibe o faturamento total por loja
