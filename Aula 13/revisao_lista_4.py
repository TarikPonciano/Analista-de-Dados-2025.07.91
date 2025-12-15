# Crie um programa que pede nome de pessoas até que o usuário digite "SAIR", ao final exiba os nomes registrados.

nomes = []

while True:

    nome = input("Digite um novo nome: ")

    if nome.upper() == "SAIR":
        print("Encerrando o programa...")
        break
    
    nomes.append(nome)

contador = 0
#len(nomes) #Tamanho da lista
#max(nomes) #Maior elemento
#min(nomes) #Menor elemento

nomes.sort()
for n in nomes:
    print(f"{contador+1}. {n}")
    contador += 1