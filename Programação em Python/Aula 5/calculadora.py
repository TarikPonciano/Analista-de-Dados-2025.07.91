# Crie um programa que pede dois números (float) ao usuário, além disso pede também uma operação (+, -, *, /). Imprima na tela a operação e o resultado da operação matemática escolhida.

num1 = float(input("Digite o primeiro número: "))

tipo_operacao = input("Digite a operação (+, -, *, /): ")

num2 = float(input("Digite o segundo número: "))

if tipo_operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado:.2f}")
elif tipo_operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado:.2f}")
elif tipo_operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado:.2f}")
elif tipo_operacao == "/":
    if num2 == 0:
        print("Não é possível dividir por zero!!!!")
    else:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado:.2f}")
else:
    print("Escolha uma operação válida!")