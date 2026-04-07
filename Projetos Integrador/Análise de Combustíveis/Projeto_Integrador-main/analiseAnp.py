import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
raw_data = pd.read_csv("Preços semestrais - AUTOMOTIVOS_2025.02.csv", sep=";")
columns_to_drop = ['CNPJ da Revenda', 'Nome da Rua','Numero Rua', 'Complemento', 'Unidade de Medida','Valor de Compra']
clean_data = raw_data.drop(columns=columns_to_drop)
clean_data["Valor de Venda"] = clean_data["Valor de Venda"].str.replace(",", ".")
clean_data["Valor de Venda"] = clean_data["Valor de Venda"].astype(float)

regioes_estados = {
    "NORDESTE": ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"],
    "NORTE": ["AC", "AP", "AM", "PA", "RO", "RR", "TO"],
    "SUL": ["PR", "RS", "SC"],
    "SUDESTE": ["ES", "MG", "RJ", "SP"],
    "CENTRO-OESTE": ["DF", "GO", "MT", "MS"]
}

st.set_page_config(layout="wide")

st.title("Análise de Combustíveis - ANP")

## Sidebar

with st.sidebar:
    st.header("Filtros")

    Regiao = st.selectbox(
        "Selecione uma região:",
        ["Todas"] + list(regioes_estados.keys())
    )


df_resultado = clean_data.copy()

## Filtros
if Regiao == "Todas":
    Estados = ["Todos"] + clean_data["Estado - Sigla"].unique().tolist()
else:
    Estados = ["Todos"] + regioes_estados[Regiao]

Estados_filtrados = st.sidebar.selectbox("Selecione um Estado:", Estados)

if Regiao != "Todas":
    df_resultado = df_resultado[
        df_resultado["Estado - Sigla"].isin(regioes_estados[Regiao])
    ]

if Estados_filtrados != "Todos":
    df_resultado = df_resultado[
        df_resultado["Estado - Sigla"] == Estados_filtrados
    ]


Produto = st.sidebar.selectbox(
    "Selecione o produto:",
    ["Todos"] + df_resultado["Produto"].unique().tolist()
)

if Produto != "Todos":
    df_resultado = df_resultado[df_resultado["Produto"] == Produto]

Bandeiras = st.sidebar.selectbox(
    "Selecione uma bandeira:",
    ["Todos"] + df_resultado["Bandeira"].unique().tolist()
)
if Bandeiras != "Todos":
    df_resultado = df_resultado[df_resultado["Bandeira"]==Bandeiras]

## cards
media_geral = df_resultado["Valor de Venda"].mean()
total_postos = df_resultado.shape[0]
total_bandeiras = df_resultado["Bandeira"].nunique()

regiao_mais_cara = (
    df_resultado.groupby("Regiao - Sigla")["Valor de Venda"]
    .mean()
    .sort_values(ascending=False)
    .index[0]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Média Geral", f"R$ {media_geral:.2f}")
col2.metric("Postos", total_postos)
col3.metric("Bandeiras", total_bandeiras)
col4.metric("Região mais cara", regiao_mais_cara)

st.divider()

## Graficos
col1, col2 = st.columns(2)

#  Concorrência
with col1:
    st.subheader("Preço vs Concorrência")

    df_grafico1 = df_resultado.groupby("Regiao - Sigla").agg(
        media_valor=("Valor de Venda", "mean"),
        concorrencia=("Bandeira", "nunique")
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(6,3))

    ax1.bar(df_grafico1["Regiao - Sigla"], df_grafico1["media_valor"], alpha=0.7, zorder=1)
    ax2 = ax1.twinx()

    ax2.plot(df_grafico1["Regiao - Sigla"], df_grafico1["concorrencia"],
             marker='o', color='red', linewidth=2.5, zorder=3)

    ax1.grid(axis='y', linestyle='--', alpha=0.3)

    st.pyplot(fig)
    st.caption("Concorrência não apresenta forte impacto no preço médio.")

# Postos
with col2:
    st.subheader("Preço vs Postos")

    df_grafico2 = df_resultado.groupby("Regiao - Sigla").agg(
        media_valor=("Valor de Venda", "mean"),
        qtd_postos=("Bandeira", "count")
    ).reset_index()

    fig, ax1 = plt.subplots(figsize=(6,3))

    ax1.bar(df_grafico2["Regiao - Sigla"], df_grafico2["media_valor"], alpha=0.7, zorder=1)
    ax2 = ax1.twinx()

    ax2.plot(df_grafico2["Regiao - Sigla"], df_grafico2["qtd_postos"],
             marker='o', color='orange', linewidth=2.5, zorder=3)

    ax1.grid(axis='y', linestyle='--', alpha=0.3)

    st.pyplot(fig)
    st.caption("Quantidade de postos apresenta maior impacto nos preços.")


df_mapa = df_resultado.groupby("Estado - Sigla").agg(
    media_valor=("Valor de Venda", "mean")
).reset_index()


# fig = px.choropleth(
#     df_mapa,
#     locations="Estado - Sigla",  
#     locationmode="geojson-id",   
#     color="media_valor",
#     scope="south america",
#     color_continuous_scale="Reds",
#     labels={"media_valor": "Preço Médio"},
# )

# ## Brasil
# fig.update_geos(
#     scope="south america",
#     center={"lat": -14, "lon": -52},
#     projection_scale=4
# )

st.divider()

## Top 5 bandeiras

st.subheader("Top 5 Bandeiras")

df_bandeiras = df_resultado["Bandeira"].value_counts().head(5)
st.bar_chart(df_bandeiras)

st.divider()


st.subheader("Distribuição de Preços")

fig, ax = plt.subplots(figsize=(7,3))
ax.hist(df_resultado["Valor de Venda"], bins=20)
st.pyplot(fig)

st.divider()

## Variação por região
st.subheader("Variação de Preços por Região")

df_var = df_resultado.groupby("Regiao - Sigla")["Valor de Venda"].std()
st.bar_chart(df_var)

st.divider()


# st.subheader("Correlação")

# df_corr = df_resultado.groupby("Regiao - Sigla").agg(
#     media=("Valor de Venda", "mean"),
#     concorrencia=("Bandeira", "nunique"),
#     postos=("Bandeira", "count")
# )

# st.dataframe(df_corr.corr())

# st.caption("Correlação valida a hipótese: postos impactam mais que concorrência.")

# st.divider()

## Maior e menor valor
# st.subheader("Destaques")

# maior_preco = df_resultado["Valor de Venda"].max()
# menor_preco = df_resultado["Valor de Venda"].min()

# st.write(f"Maior preço: R$ {maior_preco:.2f}")
# st.write(f"Menor preço: R$ {menor_preco:.2f}")

# st.divider()

## tabela top 5 menor e maior
st.subheader("Maiores Preços")

estatistica = df_resultado.groupby(
    ["Regiao - Sigla", "Estado - Sigla"]
).agg(
    media=("Valor de Venda", "mean"),
    max=("Valor de Venda", "max"),
    min=("Valor de Venda", "min")
).reset_index()

st.dataframe(estatistica.sort_values(by="media", ascending=False).head(5))

st.subheader("Menores Preços")

st.dataframe(estatistica.sort_values(by="media", ascending=True).head(5))