# 2 - Crie um programa que pede 5 números ao usuário. Ao final determine e imprima o maior número digitado.
# Bônus: Ao final exiba na tela todos os números que foram digitados

maior = None
historico = ""

for i in range(5):
    numero = int(input("Digite um número: "))
    if i == 0:
        maior = numero
        historico += f"{numero}"
    else:
        historico += f" - {numero}"

    if numero > maior:
        print(f"Número trocado: {maior} -> {numero}")
        maior = numero


print(f"O maior número digitado foi: {maior}")

print(f"Números digitados: {historico}")
