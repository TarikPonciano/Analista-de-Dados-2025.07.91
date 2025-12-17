# 3. (AVANÇADO) Ao exibir as temperaturas ordene-as de forma decrescente (maior para menor). Além disso modifique o programa para pedir 12 temperaturas, cada uma referente a um mês de 2025, ao final inclua nas informações de Maior Temperatura e Menor Temperatura o nome do mês correspondente.

temperaturas = []
meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho")

for mes in meses:
    temperatura = float(input(f"Digite a temperatura de {mes}: "))

    temperaturas.append(temperatura)



print("Lista de Temperaturas:")

contador = 0

temperaturas_ordenadas = sorted(temperaturas, reverse=True)

for t in temperaturas_ordenadas:
    print(f"{contador+1}. {t:.1f}°C ")
    contador += 1

print("RESUMO:")

maior_temperatura = max(temperaturas)
posicao_maior_temperatura = temperaturas.index(maior_temperatura)

print(f'''
Média: {sum(temperaturas)/len(temperaturas)}°C
Maior Temperatura: {max(temperaturas)}°C
Mês Maior Temperatura: {meses[posicao_maior_temperatura]}
Menor Temperatura: {min(temperaturas)}°C
''')
