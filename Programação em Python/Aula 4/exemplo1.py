# Crie um programa que recebe um número e exibe na tela se o número é par ou impar.

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print(f"O número {numero} é par!")
else:
    print(f"O número {numero} é impar!")