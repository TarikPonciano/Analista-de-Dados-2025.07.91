# Crie um programa para realização de cadastro de funcionários. O programa deverá pedir o nome de um funcionário até que seja escrito a palavra "SAIR". Ao final esse programa deve informar quantos funcionários foram cadastrados, além disso deve exibir uma lista de funcionários.

qtd_funcionarios = 0

funcionarios = []

while True:
    funcionario = input("Digite o nome do funcionário: ")

    if funcionario.upper() == "SAIR":
        print("Encerrando cadastros...")
        break

    qtd_funcionarios += 1
    funcionarios.append(funcionario)


print(f"Número de funcionários cadastrados: {qtd_funcionarios}")

print(funcionarios)