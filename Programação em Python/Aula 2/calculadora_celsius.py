# Criar um programa que:
# 1. Pede ao usuário uma temperatura em Fahrenheit
# 2. Calcula o equivalente em Celsius
# 3. Exibe o valor em Celsius

temperatura_f = float(input("Digite a temperatura em Fahrenheit: "))

temperatura_c = (temperatura_f - 32) * 5 / 9
# Arredondar Número - Método 1
#temperatura_c = round(temperatura_c,2)

print(f"A temperatura em Celsius é: {temperatura_c:.2f}°C")