import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Crie um dashboard de vendas utilizando os dados de "vendas_5000_linhas_tratado.csv"

# Deve conter pelo menos 1 filtro de categoria, ou região, ou outro critério
# Deve conter 3 métricas (Faturamento Total, Custo Total, Lucro Total ou outros)
# Deve conter 2 gráficos de análise (Faturamento pelo tempo), (Lucro por Categoria)

df = pd.read_csv("vendas_5000_linhas_tratado.csv")

st.set_page_config(page_title="Dashboard Vendas", page_icon="📊", layout="wide")

# Construindo o menu lateral

st.sidebar.header("Filtros")

categorias = ["Todos"] + df["categoria"].unique().tolist()

filtro_categoria = st.sidebar.selectbox("Escolha uma categoria:", categorias)

filtro_regiao = st.sidebar.selectbox("Escolha uma região", options=["Todos"] + df["regiao"].unique().tolist())

filtro_pagamento = st.sidebar.multiselect("Escolha uma forma de pagamento", options=df["forma_pagamento"].unique(), default=df["forma_pagamento"].unique())

# Utilize os elementos selecionados para filtrar o dataframe

if filtro_categoria != "Todos":
    df = df[df["categoria"] == filtro_categoria]

if filtro_regiao != "Todos":
    df = df[df["regiao"] == filtro_regiao]

if filtro_pagamento == []:
    filtro_pagamento = df["forma_pagamento"].unique()

df = df[df["forma_pagamento"].isin(filtro_pagamento)]


st.title("Dashboard Vendas XYZ")

st.header("2026")


# if faturamento_bruto_total > 10000000:
#     faturamento_bruto_total = faturamento_bruto_total/1000000
#     st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} milhões de reais")
# elif faturamento_bruto_total > 1000:
#     faturamento_bruto_total = faturamento_bruto_total/1000
#     st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} milhares de reais")

faturamento_bruto_total = df["total_venda"].round(2).sum()

lucro_total = df["lucro_venda"].sum()

margem_lucro = (lucro_total/faturamento_bruto_total)*100

col1, col2, col3 = st.columns([3,3,1])

with col1:
    st.metric("Faturamento Bruto", f"R$ {faturamento_bruto_total:,.2f} reais")

with col2:
    st.metric("Lucro Total", f"R$ {lucro_total:,.2f} reais")

with col3:
    st.metric("Margem de Lucro", f" {margem_lucro:.2f}%")


faturamento_por_regiao_df = df.groupby("regiao").agg(
    faturamento_total = ("total_venda", "sum")
).reset_index()

aba1, aba2, aba3, aba4 = st.tabs(["Dados 🎲", "Região 🗺️", "Categoria de Produto 🎧", "Cliente 🧑"])


# Preencha cada aba abaixo com visualizações relevantes para a categoria da aba. Cada aba deve conter 1 gráfico/tabela específico daquela situação e 2 cards de métricas. Os cards de métrica devem ser organizados usando colunas

with aba1:
    st.dataframe(df)

with aba2:
    st.subheader("EM CONSTRUÇÃO")

with aba3:
    st.subheader("EM CONSTRUÇÃO")

with aba4:
    st.subheader("EM CONSTRUÇÃO")

