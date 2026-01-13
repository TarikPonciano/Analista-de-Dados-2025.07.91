nome = input("Digite seu nome: ").strip()


if nome == "" or nome.isdigit():
    print("Inválido")
    exit()

if not nome:
    print("Inválido")

if len(nome) == 0:
    print("Inválido")