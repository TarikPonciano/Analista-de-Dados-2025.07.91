# Crie um programa que pede um palpite (0 a 100) para um jogador e repete caso o jogador erre o número secreto. Se o jogador acertar, o programa é encerrado e é exibido na tela quantos palpites foram necessários para acertar.

numero_secreto = 42

palpite = int(input("Digite um número de 0 a 100: "))
tentativas = 1

while palpite != numero_secreto:
    print("Você errou!")
    palpite = int(input("Digite um número de 0 a 100:"))
    tentativas += 1

print(f"Você venceu! O número secreto era {numero_secreto}. Você usou {tentativas} {"tentativa" if tentativas == 1 else "tentativas"}!")