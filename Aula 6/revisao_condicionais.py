# 1. Faça um Programa que leia três números e mostre-os em ordem decrescente.

def questao1():
    n1 = float(input("Digite o primeiro número: "))
    n2 = float(input("Digite o segundo número: "))
    n3 = float(input("Digite o terceiro número: "))

    if n1 > n2 and n1 > n3:
        if n2 > n3:
            print(f"{n1} > {n2} > {n3}")
        else:
            print(f"{n1} > {n3} > {n2}")
    elif n2 > n1 and n2 > n3:
        if n1 > n3:
            print(f"{n2} > {n1} > {n3}")
        else:
            print(f"{n2} > {n3} > {n1}")
    else:
        if n1 > n2:
            print(f"{n3} > {n1} > {n2}")
        else:
            print(f"{n3} > {n2} > {n1}")


# 2. Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina, mas deverá validar se o valor inserido está no intervalo descrito.