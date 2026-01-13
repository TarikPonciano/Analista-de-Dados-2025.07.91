# Crie um programa que exibe os 10 primeiros números divisíveis por 6.

# - Criar uma variável para iterar os números. Começa em 1 e a cada repetição vai aumentar 1.
numero = 1
# - Criar uma variável para contar quantos números divisíveis por 6 foram achados. Começa em 0 e a cada número que aparecer que for divisível por 6, aumentar em 1
qtd_divisiveis = 0
# - Usar um while True: para rodar a seguinte lógica
while True:
    # - Verificar se o número atual é divisivel por 6, se for divisivel por 6 exibir o número na tela e incrementar o contador da quantidade de divisíveis
    if numero % 6 == 0:
        print(numero)
        qtd_divisiveis += 1
    # - Antes de seguir para a próxima repetição, incrementar o número atual em 1
    numero += 1
    # - Ao final (dentro do while) verificar se a quantidade de divisores é maior ou igual a 10 então rodar break
    if qtd_divisiveis >= 100:
        break

