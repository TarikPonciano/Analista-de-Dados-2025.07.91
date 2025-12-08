# Crie um programa que recebe números inteiros, até que a soma desses números seja maior ou igual 100. 
# Fraseamento alternativo: Enquanto a soma dos números for menor que 100, receba novos números inteiros.

# Solução Tradicional
# soma = 0

# while soma < 100:
#     numero = int(input("Digite um número inteiro:"))
#     soma += numero

# print(f"A soma dos números é: {soma}")

# Solução Das Ruas

soma = 0

while True:
    numero = int(input("Digite um número inteiro:"))

    soma += numero

    if soma >= 100:
        break

print(f"A soma dos números é: {soma}")
    

    
