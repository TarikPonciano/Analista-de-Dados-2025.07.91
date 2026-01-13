listas = []
dicionarios = {}

temperaturas = []

for i in range(5):
    temp = float(input("Digite uma temperatura: "))
    temperaturas.append(temp)

print(f"A maior temperatura foi: {max(temperaturas)}")
print(temperaturas)