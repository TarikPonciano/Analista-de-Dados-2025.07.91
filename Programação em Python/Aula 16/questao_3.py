# 3. Faça o cadastro de um cliente, peça as informações nome, cpf, idade, gênero e altura e armazene em um dicionário. Ao final imprima as informações de forma fichada.

cliente = {
    "nome": None,
    "idade": None,
    "cpf": None,
    "genero": None,
    "altura": None
}

while True:
    novoNome = input("Digite o seu nome: ")

    if novoNome == "":
        print("Digite um nome válido!")
    else:
        break

while True:
    novoCPF = input("Digite o seu cpf:")

    if len(novoCPF) == 11:
        break
    else:
        print("Digite um cpf de tamanho válido!")

novoIdade = int(input("Digite sua idade:"))
novoGenero = input("Digite o seu gênero: ")
novoAltura = float(input("Digite sua altura: "))

cliente["nome"] = novoNome
cliente["idade"] = novoIdade
cliente["genero"] = novoGenero
cliente["cpf"] = novoCPF
cliente["altura"] = novoAltura

print("Informações do Cliente:")
for info in cliente:

    print(f"{info} - {cliente[info]}")