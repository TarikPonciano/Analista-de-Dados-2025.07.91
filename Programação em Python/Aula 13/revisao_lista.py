texto = input("Digite uma palavra:")

# texto[0]
# texto[-1]
qtd_consoantes = 0
consoantes_texto = ""

for letra in texto:
    if letra.lower() not in "aeiou":
        qtd_consoantes += 1
        consoantes_texto += letra

print(qtd_consoantes)
print(consoantes_texto)
