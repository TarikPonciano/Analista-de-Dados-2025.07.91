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

lucro_total = df["lucro_venda"].sum()

st.metric("Lucro Total", f"R$ {lucro_total:,.2f} reais")

margem_lucro = (lucro_total/faturamento_bruto_total)*100

st.metric("Margem de Lucro", f"{margem_lucro:.2f}%")

st.dataframe(df)

faturamento_por_regiao_df = df.groupby("regiao").agg(
    faturamento_total = ("total_venda", "sum")
).reset_index()

fig, axes = plt.subplots(2, 1)

axes[0].bar(faturamento_por_regiao_df["regiao"], faturamento_por_regiao_df["faturamento_total"])
axes[0].set_title("Faturamento por Tempo")
axes[0].set_xlabel("Datas")
axes[0].set_ylabel("Totais de Venda")
axes[0].grid(True, axis="y")

axes[1].bar(faturamento_por_regiao_df["regiao"], faturamento_por_regiao_df["faturamento_total"])
axes[1].set_title("Faturamento por Tempo")
axes[1].set_xlabel("Datas")
axes[1].set_ylabel("Totais de Venda")
axes[1].grid(True)


fig.tight_layout()

st.pyplot(fig)

st.bar_chart(faturamento_por_regiao_df, x="regiao", y="faturamento_total")
