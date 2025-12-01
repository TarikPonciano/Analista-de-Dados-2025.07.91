# Crie um programa que pede dois números (float) ao usuário, além disso pede também uma operação (+, -, *, /). Imprima na tela a operação e o resultado da operação matemática escolhida.

while True:

    num1 = float(input("Digite o primeiro número: "))

    tipo_operacao = input("Digite a operação (+, -, *, /): ")

    if tipo_operacao not in ["+", "-", "*", "/"]:
        print("Operação inválida")
        exit()

    num2 = float(input("Digite o segundo número: "))

    resultado = 0
    nome_operacao = ""

    if tipo_operacao == "+":
        resultado = num1 + num2
        nome_operacao = "Soma"
    elif tipo_operacao == "-":
        resultado = num1 - num2
        nome_operacao = "Subtração"
    elif tipo_operacao == "*":
        resultado = num1 * num2
        nome_operacao = "Multiplicação"
    elif tipo_operacao == "/":
        if num2 == 0:
            print("Não é possível dividir por zero!!!!")
            exit()
        else:
            resultado = num1 / num2
            nome_operacao = "Divisão"
    else:
        print("Escolha uma operação válida!")
        exit()


    print(f"O resultado da {nome_operacao} é: {num1} {tipo_operacao} {num2} = {resultado:.2f}")