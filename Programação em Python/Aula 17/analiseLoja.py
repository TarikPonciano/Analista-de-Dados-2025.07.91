import baseLoja

listaVendas = baseLoja.vendas["vendas"]

print(f"Quantidade de Vendas: {len(listaVendas)}")

totalUnidades = 0
for venda in listaVendas:
    totalUnidades += venda["quantidade"]

print(f"Total de Unidades Vendidas: {totalUnidades}")