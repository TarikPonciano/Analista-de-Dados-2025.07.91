# Criar um programa de adivinhar o número. O programa deve conter um número secreto e deverá pedir ao usuário um palpite (0 a 10), se o usuário acertar o palpite imprimir na tela vitória, se não imprimir na tela derrota.
# - Melhore o programa para exibir na tela, quando o usuário errar, se o palpite era maior ou menor que o número secreto
# - Permita que o jogador tente 3 vezes (sem usar repetições)
# - Aleatorize o número secreto sempre que o programa for iniciado

import random

numeroSecreto = random.randint(0,100)

palpite = int(input("Digite um palpite de 0 a 10: "))

if palpite == numeroSecreto:
    print(f"Você venceu de primeira! Você chutou {palpite} e o número secreto era {numeroSecreto}!")
else:
    print(f"Você perdeu! Você chutou {palpite}. Tente novamente!")
    # Criar uma nova verificação para dar dica ao jogador
    if palpite > numeroSecreto:
        print("Seu palpite foi mais alto que o número secreto!")
    else:
        print("Seu palpite foi mais baixo que o número secreto!")

    palpite = int(input("Digite seu novo palpite de 0 a 10:"))

    if palpite == numeroSecreto:
        print(f"Você venceu no segundo palpite! Você chutou {palpite} e o número secreto era {numeroSecreto}!")
    else:
        print(f"Você perdeu! Você chutou {palpite}. Tente novamente!")
        # Criar uma nova verificação para dar dica ao jogador
        if palpite > numeroSecreto:
            print("Seu palpite foi mais alto que o número secreto!")
        else:
            print("Seu palpite foi mais baixo que o número secreto!")

        palpite = int(input("Você está no palpite, chute um número de 0 a 10: "))

        if (palpite == numeroSecreto):
            print("Você acertou!")
        else:
            print("Você perdeu! Acabaram as tentativas")

            if (palpite > numeroSecreto):
                print("Seu palpite foi mais alto que o número!")
            else:
                print("Seu palpite foi mais baixo que o número!")
        
        


print("Fim de Jogo!")

print(f"O número secreto era {numeroSecreto}")