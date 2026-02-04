import pandas as pd


dados = pd.read_excel("vendas.xlsx", engine="openpyxl")

# print(dados.info())

# print(dados.isna().sum())

dados["Valor da Venda"] = dados["quantidade"] * dados["preco_unitario"]


def classificar_venda(valor):

    if valor > 1000:
        return "Alto"
    elif valor >= 300 and valor < 1000:
        return "Média"
    elif valor < 300:
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

dados["Valor Liquido"] = dados["Valor da Venda"] - dados["Imposto"]

def classificar_idade(idade):
    if idade >= 50:
        return "Sênior"
    elif idade <= 49 and idade >= 30:
        return "Adulto"
    elif idade < 30:
        return "Jovem"
    else:
        return "Idade Inválida!"

dados["Faixa Etaria"] = dados["idade"].apply(classificar_idade)

total_vendas_bruto = dados["Valor da Venda"].sum()
total_vendas_liquido = dados["Valor Liquido"].sum()
total_imposto = dados["Imposto"].sum()
num_vendas = dados["id_venda"].count()
num_vendedores = dados["vendedor"].nunique()
num_clientes = dados["cliente"].nunique()
media_venda_bruto = dados["Valor da Venda"].mean()
ticket_medio_liquido = total_vendas_liquido/num_clientes

print(f"""
RELATÓRIO DE VENDAS
===================
Total de Vendas Bruto: R$ {total_vendas_bruto:,.2f}
Total de Vendas Líquido: R$ {total_vendas_liquido:,.2f}
Total de Impostos: R$ {total_imposto:,.2f}
Número de Vendas: {num_vendas:,}
Número de Vendedores: {num_vendedores}
Número de Clientes: {num_clientes}
Média por Venda (Bruto): R$ {media_venda_bruto:,.2f}
Ticket Médio Líquido por Cliente: R$ {ticket_medio_liquido:,.2f}
""")

agrupamento_vendedor = dados.groupby("vendedor").agg(
    faturamento_bruto = ("Valor da Venda", "sum"),
    faturamento_liquido = ("Valor Liquido", "sum"),
    total_imposto = ("Imposto", "sum"),
    numero_vendas = ("id_venda", "count")
)

agrupamento_faixa_etaria = dados.groupby("Faixa Etaria").agg(
    faturamento_bruto = ("Valor da Venda", "sum"),
    faturamento_liquido = ("Valor Liquido", "sum"),
    total_imposto = ("Imposto", "sum"),
    numero_vendas = ("id_venda", "count")
)

agrupamento_nivel_venda = dados.groupby("Nivel da Venda").agg(
    faturamento_bruto = ("Valor da Venda", "sum"),
    faturamento_liquido = ("Valor Liquido", "sum"),
    total_imposto = ("Imposto", "sum"),
    numero_vendas = ("id_venda", "count")
)



print(dados.sample(10))

print(agrupamento_vendedor.sort_values("numero_vendas", ascending=False))

print(agrupamento_faixa_etaria.sort_values("numero_vendas", ascending=False))

print(agrupamento_nivel_venda.sort_values("numero_vendas", ascending=False))