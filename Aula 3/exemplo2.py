# Criar um programa de adivinhar o número. O programa deve conter um número secreto e deverá pedir ao usuário um palpite (0 a 10), se o usuário acertar o palpite imprimir na tela vitória, se não imprimir na tela derrota.
# - Melhore o programa para exibir na tela, quando o usuário errar, se o palpite era maior ou menor que o número secreto
# - Permita que o jogador tente 3 vezes (sem usar repetições)
# - Aleatorize o número secreto sempre que o programa for iniciado

numeroSecreto = 7

palpite = int(input("Digite um palpite de 0 a 10: "))

if palpite == numeroSecreto:
    print(f"Você venceu! Você chutou {palpite} e o número secreto era {numeroSecreto}!")
else:
    print(f"Você perdeu! Você chutou {palpite}. Tente novamente!")
    