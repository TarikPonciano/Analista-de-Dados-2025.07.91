import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("dados_vendas_brutos_corrigidos.xlsx", engine="openpyxl")

# Diagnóstico
# print(df.head(10))
# print(df.info())
# print(df.dtypes)
# print(df.isnull().sum())

# Ajuste e Enriquecimento de Datas

df["data"] = pd.to_datetime(df["data"], errors="coerce")

df["nome_mes"] = df["data"].dt.month_name(locale="pt_BR")
df["nome_dia"] = df["data"].dt.day_name(locale="pt_BR")
df["mes_ano"] = df["data"].dt.to_period("M")


# Criar coluna de faturamento

df["valor_venda"] = df["quantidade"] * df["preco_unitario"]


produto_venda = df.groupby("produto").agg(
    total_venda=("valor_venda", "sum")
).reset_index().sort_values("total_venda", ascending=True)

plt.figure(figsize=(12,5))

plt.plot(produto_venda["produto"], produto_venda["total_venda"])
plt.show()
