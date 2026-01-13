# 3. Faça o cadastro de um cliente, peça as informações nome, cpf, idade, gênero e altura e armazene em um dicionário. Ao final imprima as informações de forma fichada.

clientes = []

while True:
    novoCliente = {
        "nome": None,
        "idade": None,
        "cpf": None,
        "genero": None,
        "altura": None
    }

    novoCliente["nome"] = input("Digite o seu nome:")
    novoCliente["idade"] = int(input("Digite o seu idade:"))
    novoCliente["cpf"] = input("Digite o seu cpf:")
    novoCliente["genero"] = input("Digite o seu genero:")
    novoCliente["altura"] = float(input("Digite o seu altura:"))

    clientes.append(novoCliente)

    confirmar = input("DESEJA SAIR? (S/N)")

    if confirmar == "S":
        break

print("NOME | IDADE | CPF | GENERO | ALTURA")
for cliente in clientes:
    print(f"{cliente["nome"]} - {cliente["idade"]} - {cliente["cpf"]} - {cliente["genero"]} - {cliente["altura"]}")