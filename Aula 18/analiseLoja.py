import baseLoja

listaVendas = baseLoja.vendas["vendas"]

print(f"Quantidade de Vendas: {len(listaVendas)}")

totalUnidades = 0
for venda in listaVendas:
    totalUnidades += venda["quantidade"]

print(f"Total de Unidades Vendidas: {totalUnidades}")

# Produzir as métricas e exibi-las ao usuário:

# 1. Total e Média das vendas gerais
# 2. Total das vendas por categoria
# 3. Total das vendas por vendedor
# 4. Total das vendas por região