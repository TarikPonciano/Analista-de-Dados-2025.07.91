texto = "As Crônicas de Nárnia"

primeira_letra = texto[0]
ultima_letra = texto[-1]
tamanho_colecao = len(texto)

qtd_maiusculas = 0

# for i in range(len(texto)):
#     if (texto[i].isalpha()) and (texto[i] == texto[i].upper()):
#         print(f"Maiúsculo encontrado: {texto[i]}")
#         qtd_maiusculas += 1

for letra in texto:
    if letra.isalpha() and letra == letra.upper():
        print(f"Maiúsculo encontrado: {letra}")
        qtd_maiusculas += 1

print(f"Quantidade Encontrada: {qtd_maiusculas}")

