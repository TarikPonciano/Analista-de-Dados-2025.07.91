# pip install pandas openpyxl
import pandas as pd

# Monte um dicionário que contém os campos id, produto, preço, quantidade e data. Que representa uma tabela de vendas e possui 20 registros.
dados = {
    "id": list(range(1, 51)),

    "produto": [
        "Mouse", "Teclado", "Monitor", "Notebook", "Headset",
        "Webcam", "Impressora", "Mouse", "Teclado", "Monitor",
        "Notebook", "Headset", "Webcam", "Impressora", "Mouse",
        "Teclado", "Monitor", "Notebook", "Headset", "Webcam",
        "Mouse", "Teclado", "Monitor", "Notebook", "Headset",
        "Webcam", "Impressora", "Mouse", "Teclado", "Monitor",
        "Notebook", "Headset", "Webcam", "Impressora", "Mouse",
        "Teclado", "Monitor", "Notebook", "Headset", "Webcam",
        "Mouse", "Teclado", "Monitor", "Notebook", "Headset",
        "Webcam", "Impressora", "Mouse", "Teclado", "Monitor"
    ],

    "preço": [
        50, 120, 900, 3500, 200,
        150, 800, 55, 130, 950,
        3600, 210, 160, 820, 60,
        125, 920, 3400, 195, 155,
        65, 140, 980, 3700, 220,
        170, 850, 70, 135, 960,
        3550, 205, 165, 830, 75,
        145, 940, 3650, 215, 175,
        80, 150, 990, 3800, 225,
        180, 870, 85, 155, 1000
    ],

    "quantidade": [
        2, 1, 1, 1, 3,
        2, 1, 4, 2, 1,
        1, 2, 3, 1, 5,
        2, 1, 1, 4, 2,
        3, 2, 1, 1, 2,
        3, 1, 4, 2, 1,
        1, 2, 3, 1, 5,
        2, 1, 1, 4, 2,
        3, 2, 1, 1, 2,
        3, 1, 4, 2, 1
    ],

    "data": [
        "2024-01-01", "2024-01-01", "2024-01-01", "2024-01-02", "2024-01-02",
        "2024-01-02", "2024-01-03", "2024-01-03", "2024-01-03", "2024-01-04",
        "2024-01-04", "2024-01-04", "2024-01-05", "2024-01-05", "2024-01-05",
        "2024-01-06", "2024-01-06", "2024-01-06", "2024-01-07", "2024-01-07",
        "2024-01-07", "2024-01-08", "2024-01-08", "2024-01-08", "2024-01-09",
        "2024-01-09", "2024-01-09", "2024-01-10", "2024-01-10", "2024-01-10",
        "2024-01-11", "2024-01-11", "2024-01-11", "2024-01-12", "2024-01-12",
        "2024-01-12", "2024-01-13", "2024-01-13", "2024-01-13", "2024-01-14",
        "2024-01-14", "2024-01-14", "2024-01-15", "2024-01-15", "2024-01-15",
        "2024-01-16", "2024-01-16", "2024-01-17", "2024-01-17", "2024-01-18"
    ]
}

tabela_vendas = pd.DataFrame(dados)

#Visualiza a tabela por completo
#print(tabela_vendas)

#Ver as n primeiras linhas de uma tabela
# print(tabela_vendas.head(1))

#Ver as n últimas linhas de uma tabela
# print(tabela_vendas.tail(1))

#Ver n linhas aleatórias
#print(tabela_vendas.sample(5))

# Exibe quantas linhas a tabela possui
#print(tabela_vendas.shape[0])
# Exibe quantas coluna a tabela possui
#print(tabela_vendas.shape[1])

# Informações das colunas, tipos de dados e memória
# tabela_vendas.info()

# # Mostra a lista das colunas
# print(tabela_vendas.columns)
# # Exibe as colunas e os tipos de dados
# print(tabela_vendas.dtypes)
# # Exibe o intervalo utilizado para identificar linhas específicas
# print(tabela_vendas.index)

# Conjunto pré montado de agregados numéricos
# print(tabela_vendas.describe())

# print(f"Média de Preços: {tabela_vendas["preço"].mean()}")
# print(f"Soma de Preços: {tabela_vendas["preço"].sum()}")
# print(f"Menor Preço: {tabela_vendas["preço"].min()}")
# print(f"Maior Preço: {tabela_vendas["preço"].max()}")
# print(f"Desvio Padrão Preço: {tabela_vendas["preço"].std()}")
# print(f"Mediana Preço: {tabela_vendas["preço"].median()}")

tabela_vendas["Total da Venda Bruto"] = tabela_vendas["preço"] * tabela_vendas["quantidade"]

tabela_vendas["Valor de Desconto"] = tabela_vendas["Total da Venda Bruto"] * 0.1

tabela_vendas["Total da Venda"] = tabela_vendas["Total da Venda Bruto"] - tabela_vendas["Valor de Desconto"]


# print(tabela_vendas)

# Total do faturamento
print(f"Faturamento Total: R$ {tabela_vendas["Total da Venda"].sum():.2f}")
# Maior Venda
print(f"Maior Venda: R$ {tabela_vendas["Total da Venda"].max():.2f}")
# Menor Venda
print(f"Menor Venda: R$ {tabela_vendas["Total da Venda"].min():.2f}")
# Média das vendas
print(f"Média de Faturamento: R$ {tabela_vendas["Total da Venda"].mean():.2f}")


tabela_vendas = tabela_vendas.rename(columns={"preço": "Preço R$", "quantidade": "Quantidade", "id": "ID", "produto": "Produto"})

tabela_vendas["Preço R$"] = tabela_vendas["Preço R$"].astype("float64")

# print(tabela_vendas[["Preço R$", "Quantidade"]])

# # Acessa os dados de uma linha específica
# print(tabela_vendas.iloc[0])

# # Acessa os dados de um intervalo de linhas
# print(tabela_vendas.iloc[2:5])

# # Acessa a última linha

# print(tabela_vendas.iloc[-1])


# Seleção de Linhas por condicionais

# print(tabela_vendas[tabela_vendas["Total da Venda"] > 1000])

# Exiba uma tabela resultante das vendas que tiveram 2 ou mais unidades vendidas.
print(tabela_vendas[tabela_vendas["Quantidade"] >= 2])

# Exiba o faturamento total das vendas de Notebook
tabela_notebooks = tabela_vendas[ tabela_vendas["Produto"] == "Notebook"]
print(tabela_notebooks)

faturamento_notebooks = tabela_notebooks["Total da Venda"].sum()
print(f"Faturamento das vendas de Notebook: {faturamento_notebooks}")

# Exiba a média das vendas de Mouse que ultrapassaram 2 unidades

tabela_mouse_2unidades = tabela_vendas[(tabela_vendas["Produto"] == "Mouse") & (tabela_vendas["Quantidade"] >= 2)]

print(tabela_mouse_2unidades)

media_vendas_mouse_2unidades = tabela_mouse_2unidades["Total da Venda"].mean()

print(media_vendas_mouse_2unidades)


faturamento_total = tabela_vendas["Total da Venda"].sum()

tabela_vendas["Participação do Faturamento"] = (tabela_vendas["Total da Venda"] / faturamento_total)*100

print(tabela_vendas)

tabela_vendas.to_excel('teste.xlsx', index=False)