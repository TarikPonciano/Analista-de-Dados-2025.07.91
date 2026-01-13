# Crie um programa que pede um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "password", exiba na tela "Acesso Concedido", se não exiba "Acesso Negado"

usuario = input("Digite o nome do usuário:")

if usuario != "admin":
    print("Usuário não encontrado")
    exit()

senha = input("Digite a senha do usuário:")

if senha == "password":
    print("Acesso Concedido!")
else:
    print("Acesso Negado!")