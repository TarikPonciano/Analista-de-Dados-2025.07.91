# Para rodar a página executar no servidor:
# streamlit run appSimples.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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

lojas = ["Todos"] + df["lojas"].unique().tolist()

loja = st.selectbox("Escolha uma loja: ", lojas)

dfLojas = df.copy()[df["lojas"] == loja]

# Produzir uma tabela (groupby) que exibe o faturamento total por loja

df_faturamento_loja = df.groupby("lojas").agg(
    faturamento_total=("vendas", "sum")
).reset_index()

if loja == "Todos":
    st.dataframe(df)
    st.dataframe(df_faturamento_loja)
else:
    st.dataframe(dfLojas)
    st.dataframe(df_faturamento_loja.copy()[df_faturamento_loja["lojas"] == loja])

# Exibir na tela do nosso streamlit o Faturamento Total Geral

faturamento_geral = df["vendas"].sum()

faturamento_filtrado = dfLojas["vendas"].sum()

st.metric(f"Percentual de Participação da {loja}", f"{((faturamento_filtrado/faturamento_geral)*100):.1f}%")

st.metric("Faturamento Geral", f"R$ {faturamento_geral:,.2f}")

st.divider()

# Produzir um gráfico de vendas por mês
st.header("Gráficos")

# Cria a "figura" do gráfico
fig, ax = plt.subplots()

# Usar o ax para configurar o gráfico 
ax.plot(df["meses"], df["vendas"], marker="o")

ax.set_ylim(bottom=0, top=df["vendas"].max()+500)
ax.set_xlabel("Meses")
ax.set_ylabel("Faturamento")
ax.set_title("Faturamento por Mês")
ax.grid(True)

# Pede para o streamlit exibir a "figura"
st.pyplot(fig)

