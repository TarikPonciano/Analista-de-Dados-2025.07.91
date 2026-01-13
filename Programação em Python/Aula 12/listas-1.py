# Crie um programa que pede a idade de 10 pessoas. Armazene essas idades em uma lista e calcule a média de idade, a menor idade, a maior idade e quantas pessoas possuem idade maior ou igual a 30 anos.
# Crie uma lista antes das repetições
# Use o comando .append para adicionar elementos na lista

lista_idades = []

for i in range(10):
    idade = int(input("Digite uma idade: "))

    lista_idades.append(idade)

print(f"Idades coletadas: {lista_idades}")

# media_idade = 0
# soma_idade = 0
# qtd_idade = 0

# menor_idade = lista_idades[0]

# maior_idade = lista_idades[0]

# qtd_maior_que_30 = 0

# for idade in lista_idades:

#     soma_idade += idade
#     qtd_idade += 1

#     if idade < menor_idade:
#         menor_idade = idade

#     if idade > maior_idade:
#         maior_idade = idade

#     if idade >= 30:
#         qtd_maior_que_30 += 1

media_idade = sum(lista_idades)/len(lista_idades)
maior_idade = max(lista_idades)
menor_idade = min(lista_idades)

qtd_maior_que_30 = 0

for idade in lista_idades:

    if idade >= 30:
        qtd_maior_que_30 += 1


print(f'''
Resultados da Análise:
      
      Maior Idade: {maior_idade}
      Menor Idade: {menor_idade}
      Média Idade: {media_idade}
      Pessoas a partir de 30 anos: {qtd_maior_que_30}

''')

