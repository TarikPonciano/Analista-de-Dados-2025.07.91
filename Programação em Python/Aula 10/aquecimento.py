# Crie um programa que exibe um menu com 3 charadas e uma opção de sair. Ao escolher uma das opções do menu, exibe a charada escolhida e pede uma resposta ao jogador. Se o jogador acertar é exibida uma mensagem de vitória, se o jogador errar é exibida uma mensagem de derrota. Independente do resultado, volta ao menu depois do palpite.

# Bônus: Imprima um tela de vitória especial para quando o jogador resolver as 3 charadas.

acerto_1 = False
acerto_2 = False
acerto_3 = False

while True:
    print('''
Seja bem vindo à Tumba da Esfinge

Escolha uma opção abaixo:
          
    1. Charada 1
    2. Charada 2
    3. Charada 3
    
    0. Sair
''')
    op = input("Digite o número desejado:")

    if op == "1":
        print("----- CHARADA 1 -----")
        print("O que é o que é surdo e mudo e conta tudo?")
        palpite = input("Digite seu palpite: ")

        if palpite == "livro":
            print("A resposta está correta!")
            acerto_1 = True
            
        else:
            print("Você errou! Sua alma será amaldiçoada pela eternidade!")

    elif op == "2":
        print("----- CHARADA 2 -----")
        print("O que é o que é cai em pé e corre deitado?")
        palpite = input("Digite seu palpite: ")

        if palpite == "chuva":
            print("A resposta está correta!")
            acerto_2 = True
        else:
            print("Você errou! Sua alma será amaldiçoada pela eternidade!")
    elif op == "3":
        print("----- CHARADA 3 -----")
        print("Que criatura tem 4 pernas de manhã, 2 a tarde e 3 a noite?")
        palpite = input("Digite seu palpite: ")

        if palpite == "homem":
            print("A resposta está correta!")
            acerto_3 = True
        else:
            print("Você errou! Sua alma será amaldiçoada pela eternidade!")
    elif op == "0":
        print("Saindo do programa... ")
        break
    else:
        print("Digite uma opção válida do menu!")

    if acerto_1 and acerto_2 and acerto_3:
        print("Você ascendeu ao topo da sociedade Egípcia. MEU FARAÓ!")
        break


    input("DIGITE ENTER PARA CONTINUAR")