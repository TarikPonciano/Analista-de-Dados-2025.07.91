nomes = ["Pelé", "Garrincha", "Maradona", "Kaká"]
nomes[2] = "Ronaldo Fenômeno"
nomes.append("Ronaldinho Gaúcho")
nomes.pop(0)

"""
Exemplo:

1. Pelé
2. Garrincha
3. Maradona
"""
print("Nomes: ")
contador = 0
for nome in nomes:
    print(f"{contador+1}. {nome}")
    contador += 1

'''
CRUD
CREATE
READ
UPDATE
DELETE
'''

# Inserir dado na lista

# lista.append(novoElemento)

# Ler um dado da lista

# lista[indice]

# Atualizar um dado na lista

# lista[indice] = "Novo Elemento"

# Remover dado na lista

# lista.pop(indice)