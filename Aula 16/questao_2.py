# 2. Crie um dicionário que organiza os contatos telefônicos de alguém. Como chave você deverá utilizar o nome da pessoa e como valor, o telefone da pessoa. Crie 5 contatos e exiba somente o telefone de um contato chamado "Mario".

agenda = {
    "José": "123456897",
    "Michel": "123156465",
    "Josefina": "5456456689",
    "Mario": "486489848469",
    "Clayton": "56656165516"
}

print("Lista de Contatos:")
contador = 1
for chave in agenda:
    print(f"{contador}. {chave}")
    contador+=1


opcao = int(input("Digite o número da opção desejada:"))

contato = list(agenda.keys())[opcao-1]

print(f"{contato} - {agenda[contato]}")


# Acessando usando nome
# contato = input("Digite o nome do contato: ")

# if contato in agenda:
#     print(agenda[contato])
# else:
#     print("Contato não encontrado.")

# Maneira alternativa

# print(agenda.get(contato, "Contato não encontrado."))