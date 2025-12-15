# 1. (BÁSICO) Crie um programa que pede o nome de 5 frutas e ao final imprime uma lista numerada com o nome das frutas. Exemplo:

# 1. Fruta 1
# 2. Fruta 2
# 3. Fruta 3
# 4. Fruta 4
# 5. Fruta 5

# 1. (AVANÇADO) Continue o programa anterior e agora ao lado do nome de cada fruta acrescente o texto "é saudável!"

frutas = []

# for i in range(5):
#     fruta = input("Digite o nome de uma fruta:")
#     frutas.append(fruta)

while True:

    fruta = input("Digite o nome de uma fruta:")

    if len(fruta) > 0:
        frutas.append(fruta)
    else:
        print("Escreva algo no campo nome da fruta!")

    if len(frutas) >= 5:
        print("Frutas cadastradas!")
        break


contador = 0
# frutas.sort(reverse=True)
for fruit in frutas:
    print(f"{contador+1}. {fruit} é saudável!")
    contador += 1