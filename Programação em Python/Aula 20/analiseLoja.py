# Carregar dados da base Loja, exibir a lista de vendas e exibir o total de vendas realizadas.

# Carregar dados
import baseLoja

lista_vendas = baseLoja.vendas["vendas"]

# Exibir a lista de Vendas
print("Lista de Vendas:")
print("ID | Produto | Categoria | Valor Unitário(R$) | Quantidade")

for venda in lista_vendas:
    print(f"{venda["id"]} | {venda["produto"]} | {venda["categoria"]} | R$ {venda["valor_unitario"]:.2f} | {venda["quantidade"]}")

# Produzir as métricas e exibi-las ao usuário:
print()
print("------- RESUMO ------")
# 1. Total e Média das vendas gerais

total_geral = 0
media_geral = 0

for venda in lista_vendas:
    total_geral += venda["quantidade"] * venda["valor_unitario"]

media_geral = total_geral/len(lista_vendas)

print(f"Total das vendas: R$ {total_geral:.2f}")
print(f"Ticket Médio: R$ {media_geral}")
print(f"Quantidade de Vendas: {len(lista_vendas)}")

#Exibir total de unidades vendidas
total_unidades = 0
for venda in lista_vendas:
    total_unidades += venda["quantidade"]

print(f"Total de Unidades Vendidas: {total_unidades}")

#Maior e Menor Venda
maior_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 
menor_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 

for venda in lista_vendas:
    total_venda = venda["quantidade"] * venda["valor_unitario"]

    if total_venda > maior_venda:
        maior_venda = total_venda

    if total_venda < menor_venda:
        menor_venda = total_venda

print(f"Maior Valor de Venda: R$ {maior_venda}")
print(f"Menor Valor de Venda: R$ {menor_venda}")

#Exibir o nome dos Vendedores e a quantidade de vendedores
print("-------------------------------------------")
lista_vendedores = []
print("Lista de Vendedores:")
for venda in lista_vendas:
    if venda["vendedor"] not in lista_vendedores:
        lista_vendedores.append(venda["vendedor"])

lista_vendedores.sort()
for vendedor in lista_vendedores:
    print(vendedor)

print(f"Quantidade de Vendedores: {len(lista_vendedores)}")
#Exibir o nome das Regiões e a quantidade de regiões
print("-------------------------------------------")
lista_regioes = []
print("Lista de Regiões:")
for venda in lista_vendas:
    if venda["regiao"] not in lista_regioes:
        lista_regioes.append(venda["regiao"])

lista_regioes.sort()

for contador, regiao in enumerate(lista_regioes):
    print(f"{contador+1}. {regiao}")
    

print(f"Quantidade de Regiões: {len(lista_regioes)}")

#Exibir a quantidade de vendas que superou a meta de venda de 3000 reais
meta_atingida_qtd = 0
meta_atingida_vendas = []

for venda in lista_vendas:
    total_venda = venda["quantidade"] * venda["valor_unitario"]
    if total_venda >= 3000:
        meta_atingida_qtd += 1
        meta_atingida_vendas.append(venda)
        
meta_atingida_total_venda = 0
for venda in meta_atingida_vendas:
    print(venda)
    meta_atingida_total_venda += venda["quantidade"] * venda["valor_unitario"]

print(f"Vendas acima da meta: {meta_atingida_qtd}")
print(f"Total obtido com vendas acima da meta: R$ {meta_atingida_total_venda:.2f}")

# 2. Total das vendas por categoria
vendas_por_categoria = {
}
for venda in lista_vendas:
    if venda["categoria"] not in vendas_por_categoria:
        vendas_por_categoria[venda["categoria"]] = 0

    vendas_por_categoria[venda["categoria"]] += venda["quantidade"] * venda["valor_unitario"]

print("Total por Categoria:")
for categoria in vendas_por_categoria:
    print(f"{categoria} - R$ {vendas_por_categoria[categoria]:.2f}")

# 3. Total das vendas por vendedor

vendas_por_vendedor = {
}
for venda in lista_vendas:
    if venda["vendedor"] not in vendas_por_vendedor:
        vendas_por_vendedor[venda["vendedor"]] = 0

    vendas_por_vendedor[venda["vendedor"]] += venda["quantidade"] * venda["valor_unitario"]

print("Total por Vendedor:")
for vendedor in vendas_por_vendedor:
    print(f"{vendedor} - R$ {vendas_por_vendedor[vendedor]:.2f}")


# 4. Total das vendas por região