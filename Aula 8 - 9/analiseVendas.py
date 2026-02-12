# %% [markdown]
# Analise Venda

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# Leitura de Dados

# %%
df = pd.read_excel("dados_vendas_brutos_corrigidos.xlsx", engine="openpyxl")

# %% [markdown]
# Visualização dos Dados

# %%
display(df.sample(10))
display(df.info())
display(df.dtypes)
display(df.isnull().sum())

# %% [markdown]
# Limpeza e Análise das Datas

# %%
df["data"] = pd.to_datetime(df["data"], errors="coerce")

df["nome_mes"] = df["data"].dt.month_name(locale="pt_BR")
df["nome_dia"] = df["data"].dt.day_name(locale="pt_BR")
df["mes_ano"] = df["data"].dt.to_period("M")

# %% [markdown]
# Enriquecimento da Coluna Valor Venda

# %%
df["valor_venda"] = df["quantidade"] * df["preco_unitario"]

# %% [markdown]
# Gráfico Produto Venda

# %%
produto_venda = df.groupby("produto").agg(
    total_venda=("valor_venda", "sum")
).reset_index().sort_values("total_venda", ascending=False)

plt.figure(figsize=(12,5))

plt.bar(produto_venda["produto"], produto_venda["total_venda"], color="red")
plt.show()

# %%
produto_venda = df.groupby("produto").agg(
    total_venda=("valor_venda", "sum")
).reset_index()

plt.plot(produto_venda["produto"], produto_venda["total_venda"])
plt.show()


