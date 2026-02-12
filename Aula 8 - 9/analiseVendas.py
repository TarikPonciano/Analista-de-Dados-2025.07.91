# %% [markdown]
# # Analise Venda

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# # Leitura de Dados

# %%
df = pd.read_excel("dados_vendas_brutos_corrigidos.xlsx", engine="openpyxl")

# %% [markdown]
# Visualização dos Dados

# %%
# display(df.sample(10))
# display(df.info())
# display(df.dtypes)
# display(df.isnull().sum())

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

# %% [markdown]
# Gráfico de Barras Faturamento por Loja

# %%
faturamento_loja = df.groupby("loja").agg(
    total_venda = ("valor_venda", "sum")
).reset_index().sort_values("total_venda", ascending=True)


cores = plt.cm.tab10(range(len(faturamento_loja["loja"])))

plt.figure(figsize=(15,5))

barras = plt.bar(faturamento_loja["loja"], faturamento_loja["total_venda"], color = cores)

plt.title("Loja X Faturamento")

plt.xlabel("Lojas")
plt.ylabel("Faturamento")

plt.grid(True, axis="y", alpha=0.3)


for bar in barras:
    plt.text(
        bar.get_x() + bar.get_width()/2,
        bar.get_height(),
        f"R$ {bar.get_height():,.2f}",
        ha="center",
        va="bottom"

    )


plt.show()


