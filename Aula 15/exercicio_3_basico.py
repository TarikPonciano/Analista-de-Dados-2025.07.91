# 3. (BÁSICO) Crie um programa que recebe uma lista de valores de temperatura. O usuário deverá escrever cada temperatura até que escreva "SAIR" no campo de cadastro. Ao finalizar exibir a lista de temperaturas, a maior temperatura, a menor temperatura e a média de temperatura.

temperaturas = []

while True:
    temperatura = input("Digite a temperatura:")
    
    if temperatura.upper() == "SAIR":
        print("Finalizando cadastro...")
        break
    
    temperaturas.append(float(temperatura))

print("Lista de Temperaturas:")

contador = 0
maior_temperatura = temperaturas[0]
menor_temperatura = temperaturas[0]
soma_temperaturas = 0

for t in temperaturas:
    print(f"{contador+1}. {t:.1f}°C ")
    soma_temperaturas += t

    if t > maior_temperatura:
        maior_temperatura = t
    if t < menor_temperatura:
        menor_temperatura = t

    contador += 1

print("RESUMO Funções:")

print(f'''
Média: {sum(temperaturas)/len(temperaturas)}°C
Maior Temperatura: {max(temperaturas)}°C
Menor Temperatura: {min(temperaturas)}°C
''')


print("RESUMO Caseiro:")
print(f'''
Média: {soma_temperaturas/contador}°C
Maior Temperatura: {maior_temperatura}°C
Menor Temperatura: {menor_temperatura}°C
''')