texto = "Abacate"

print("Primeira letra:",texto[0])
#Crie uma variável contendo uma palavra, imprima na tela apenas a última letra
print("Última letra:", texto[-1])
print("Letra do meio:", texto[int(len(texto)/2)])

print("Tamanho do texto:", len(texto))

for i in range(len(texto)):
    letra = texto[i]

    # if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    #     print(letra)

    if letra in "aeiou":
        print(letra)


# Crie um programa que pede 5 nomes de cachorro. Contabilize quantos nomes começam com vogal. Ao final exiba a contagem de nomes:
    