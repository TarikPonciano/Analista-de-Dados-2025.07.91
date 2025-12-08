# Crie um programa que pede um palpite (0 a 100) para um jogador e repete caso o jogador erre o número secreto. Se o jogador acertar, o programa é encerrado e é exibido na tela quantos palpites foram necessários para acertar.

# Missão 1: Ao errar, dê uma dica para o jogador. Informe se o número secreto é maior ou menor que o palpite.

# Missão 2: Encerre o jogo após 3 tentativas. Caso o jogador não acerte, exiba uma mensagem de Derrota.

#Missão 3: Faça com que o número secreto seja aleatório e o número mude sempre que for iniciado um novo jogo

#Missão 4: Ao final do jogo, pergunte se o jogador deseja jogar novamente e reinicie o jogo

numero_secreto = 42
tentativas = 0

while True:
    
    palpite = int(input("Digite um número de 0 a 100:"))
    tentativas += 1

    if palpite == numero_secreto:
        break
    else:
        print("Você errou!")


print(f"Você venceu! O número secreto era {numero_secreto}. Você usou {tentativas} {"tentativa" if tentativas == 1 else "tentativas"}!")