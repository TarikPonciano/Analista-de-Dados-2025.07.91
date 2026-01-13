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

def questao2():

    valor_saque = int(input("Digite o valor do saque: "))

    if valor_saque < 10 or valor_saque > 600:
        print("Valor inválido. Digite um saque de 10 a 600 reais!")
        exit()

    notas1 = 0
    notas5 = 0
    notas10 = 0
    notas50 = 0
    notas100 = 0

    restante = valor_saque

    if restante >= 100:
        # Levando em consideração 534
        notas100 = int(restante/100) # 5 notas de 100
        restante = restante % 100 # sobrou 34 para ser contado

    if restante >= 50:
        notas50 = int(restante/50)
        restante = restante % 50

    if restante >= 10:
        # Sobrou 34 da operação anterior
        notas10 = int(restante/10) # 3 notas de 10
        restante = restante % 10 # sobrou 4 para ser contado

    if restante >= 5:
        notas5 = int(restante/5)
        restante = restante % 5 

    if restante >= 1:
        notas1 = int(restante/1)
        restante = restante % 1   

    print(f'''

    O valor de R$ {valor_saque:.2f} pode ser dividido nas seguintes notas:

    Notas de 100: {notas100}
    Notas de 50: {notas50}
    Notas de 10: {notas10}
    Notas de 5: {notas5}
    Notas de 1: {notas1}

    ''')

