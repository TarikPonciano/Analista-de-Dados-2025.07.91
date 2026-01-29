import ConexaoDB
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

DB_NAME = os.getenv("DB_NAME")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

meuBanco = ConexaoDB.ConexaoDB(DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD)

print("Bem vindo ao Sistema de Gerenciamento XYZ")
while True:
    print('''
    MENU DE OPÇÕES:

          1. Ver Livros
          2. Cadastrar Livro

          0. SAIR
''')
    op = input("Digite a opção desejada:")

    if op == "0":
        print("Saindo do Programa...")
        break
    elif op == "1":
        print("VER LIVROS")
        livros = meuBanco.consultar('''
    SELECT * FROM "Livro";
''')    
        for livro in livros:
            print(livro)

    elif op == "2":
        print("CADASTRAR LIVRO")
    else:
        print("Digite novamente! Opção INVÁLIDA!")

    input("TECLE ENTER PARA CONTINUAR")