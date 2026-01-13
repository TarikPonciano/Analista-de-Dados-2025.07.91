# Crie um programa que recebe a idade de um usuário. Categorize se a pessoa é jovem ou adulto seguindo o critério abaixo:
# Menor que 18 anos, Jovem
# 18 anos ou mais, Adulto

# idade = int(input("Digite sua idade: "))

# if idade < 18:
#     print("Você é jovem!")
# else:
#     print("Você é adulto!")

# Nível 2: Categorize agora em mais faixas de idade:

# Menor que 18, Jovem
# 18 anos ou mais e menor que 65, Adulto
# Acima de 65, Sênior

idade = int(input("Digite sua idade: "))

if idade < 18 and idade >= 0:
    print("Você é jovem 🧒!")
elif idade >= 18 and idade < 65:
    print("Você é adulto 👩!")
elif idade >= 65:
    print("Você é sênior 👴!")
else:
    print("Você é alienigena 👽!")