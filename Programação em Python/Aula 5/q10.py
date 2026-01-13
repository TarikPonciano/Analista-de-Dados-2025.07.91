print("Cálculo de Bônus Empresa XYZ")

nota_desempenho = input("Digite o desempenho do funcionário (0 a 10):")

if nota_desempenho.isdigit():
    nota_desempenho = int(nota_desempenho)
else:
    print("Digite apenas números!")
    exit()

if nota_desempenho > 10 or nota_desempenho < 0:
    print("Nota inválida. Tente novamente usando entre 0 e 10.")
    exit()

anos_empresa = int(input("Digite quantos anos de empresa o funcionário possui: "))

bonus = 0
nivel_desempenho = ""

if nota_desempenho < 6:
    bonus = 0
    nivel_desempenho = "Baixo"
elif nota_desempenho >= 6 and nota_desempenho <= 8:
    nivel_desempenho = "Médio"
    if anos_empresa < 2:
        bonus = 500
    else:
        bonus = 1000
else:
    nivel_desempenho = "Alto"
    if anos_empresa < 2:
        bonus = 2000
    else:
        bonus = 3000

print(f"O desempenho desse funcionário foi: {nivel_desempenho}")
print(f"O bônus desse funcionário deve ser de: R$ {bonus:.2f}")
