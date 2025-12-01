# Crie um programa que pede um nome de usuário e uma senha. Se o nome de usuário for "admin" e a senha for "password", exiba na tela "Acesso Concedido", se não exiba "Acesso Negado"

usuario = input("Digite o login de usuário:")
senha = input("Digite a senha do usuário:")

if usuario == "admin" and senha == "password":
    print("Acesso Concedido")
else:
    print("Acesso Negado")