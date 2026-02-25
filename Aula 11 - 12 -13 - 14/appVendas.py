import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Crie um dashboard de vendas utilizando os dados de "vendas_5000_linhas_tratado.csv"

# Deve conter pelo menos 1 filtro de categoria, ou região, ou outro critério
# Deve conter 3 métricas (Faturamento Total, Custo Total, Lucro Total ou outros)
# Deve conter 2 gráficos de análise (Faturamento pelo tempo), (Lucro por Categoria)

df = pd.read_csv("vendas_5000_linhas_tratado.csv")

st.set_page_config(page_title="Dashboard Vendas", page_icon="📊")

st.title("Dashboard Vendas XYZ")
st.header("2026")

categorias = ["Todos"] + df["categoria"].unique().tolist()

filtro_categoria = st.selectbox("Escolha uma categoria:", categorias)

if filtro_categoria != "Todos":
    df = df[df["categoria"] == filtro_categoria]

faturamento_bruto_total = df["total_venda"].round(2).sum()

# if faturamento_bruto_total > 10000000:
#     faturamento_bruto_total = faturamento_bruto_total/1000000
#     st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} milhões de reais")
# elif faturamento_bruto_total > 1000:
#     faturamento_bruto_total = faturamento_bruto_total/1000
#     st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} milhares de reais")

st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} reais")



st.dataframe(df)


