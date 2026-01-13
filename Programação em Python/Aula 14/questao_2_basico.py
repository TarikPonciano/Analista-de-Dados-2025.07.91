# 2. (BÁSICO) Crie um programa que pede o nome de um aluno, seu cpf e idade além de 4 notas VÁLIDAS (0 a 10) desse aluno. Ao final imprima uma ficha com as informações pessoais desse aluno, sua média, situação(aprovado, recuperação ou reprovado) e um boletim com as notas inseridas em sequência. Exemplo:
"""
==================================================
FICHA DO ALUNO
==================================================
Nome: João Silva
CPF: 123.456.789-00
Idade: 16
--------------------------------------------------
BOLETIM ESCOLAR
Nota 1: 8.5
Nota 2: 7.0
Nota 3: 9.0
Nota 4: 6.5
--------------------------------------------------
Média: 7.8
Situação: Aprovado
==================================================
"""

# 2. (AVANÇADO) Faça uma versão alternativa do programa anterior que cadastra uma lista de alunos. Cada aluno deve ter seu nome fornecido e 4 notas válidas. Ao final exiba uma lista numerada com Nome - Notas - Média - Situação para cada aluno cadastrado. Exiba também a média geral dos alunos, a maior média e a menor média.


print("GERENCIAMENTO DE SALA DE AULA XYZ")

print("Cadastro de aluno:")

nome = input("Digite o nome do aluno: ")
cpf = input("Digite o cpf do aluno: ")
idade = int(input("Digite sua idade: "))

notas = []

while True:
    nota = float(input(f"Digite a nota {len(notas)+1} (0 a 10): "))

    if nota >= 0 and nota <=10:
        notas.append(nota)
    else:
        print("Digite uma nota válida! Tente novamente...")
        continue

    if len(notas) >= 4:
        print("Notas cadastradas!")
        print(f"DEBUG: {notas}")
        break
        
media = sum(notas)/len(notas)

situacao = "DESCONHECIDO"

if media >= 7 and media <= 10:
    situacao = "APROVADO"
elif media >= 4 and media < 7:
    situacao = "RECUPERAÇÃO"
elif media >= 0 and media < 4:
    situacao = "REPROVADO"
else:
    situacao = "ERRO DE CATEGORIZAÇÃO"


print(f'''
==================================================
FICHA DO ALUNO
==================================================
Nome: {nome}
CPF: {cpf}
Idade: {idade}
--------------------------------------------------
BOLETIM ESCOLAR
''')

contador = 0
for n in notas:
    print(f"Nota {contador+1}: {n:.1f}")
    contador += 1

# Outra forma de iterar
# for i in range(len(notas)):
#     print(f"Nota {i+1}: {notas[i]}")

print(f'''
--------------------------------------------------
Média: {media:.1f}
Situação: {situacao}
==================================================
''')