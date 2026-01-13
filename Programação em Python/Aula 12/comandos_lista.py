nomes = ["Marcelo", "Francivaldo", "Leudo", "Ariane"] # Ordenada e mutável

print(nomes[3]) # Acessa a posição 3 e imprime "Ariane"

nomes.append("Sara") # Adiciona elemento ao final da lista
nomes.insert(0, "Lucas")

print(nomes) # Imprime a lista completa
#['Lucas', 'Marcelo', 'Francivaldo', 'Leudo', 'Ariane', 'Sara']

nomes[3] = "Mônica" #Substitui um elemento

print(nomes)

nomes.remove("Ariane") # Remove um elemento específico
print(nomes.pop()) # Remove o elemento na posição indicada. Se não for informado, remove o último. Também retorna o último elemento removido

print(nomes)
