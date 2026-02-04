import pandas as pd


dados = pd.read_excel("vendas.xlsx", engine="openpyxl")

# print(dados.info())

# print(dados.isna().sum())

dados["Valor da Venda"] = dados["quantidade"] * dados["preco_unitario"]


def classificar_venda(valor):

    if valor > 500:
        return "Alto"
    elif valor >= 100 and valor < 500:
        return "Média"
    elif valor < 100:
        return "Baixo"
    else:
        return "Venda Inválida!"

dados["Nivel da Venda"] = dados["Valor da Venda"].apply(classificar_venda)

def calcular_imposto(valor):
    if valor > 300:
        return valor * 0.15
    else:
        return valor * 0.1

dados["Imposto"] = dados["Valor da Venda"].apply(calcular_imposto)

# dados["Imposto %"] = 0.1

# dados.loc[dados["Valor da Venda"]>300, "Imposto %"] = 0.15

# dados["Imposto"] = dados["Valor da Venda"] * dados["Imposto %"]

dados["Valor Líquido"] = dados["Valor da Venda"] - dados["Imposto"]

print(dados.sample(10))

agrupamento_vendedor = dados.groupby("vendedor").agg(
    faturamento_total=("Valor da Venda", "sum")
) 

print(agrupamento_vendedor.sort_values("faturamento_total", ascending=False).head(3))