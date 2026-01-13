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

# 2. (AVANÇADO) Faça uma versão alternativa do programa anterior que cadastra uma lista de alunos. Cada aluno deve ter seu nome fornecido e 4 notas válidas. Ao final exiba uma lista numerada com Nome - Notas - Média - Situação para cada aluno cadastrado. 

print("BEM VINDO AO SISTEMA ESCOLAR XYZ")
alunos = [
    ["João", [10,5,8,9]]
]

while True:
    novoAluno = []

    nome = input("Digite seu nome: ")

    if nome.upper() == "SAIR":
        print("Encerrando o programa...")
        break

    novoAluno.append(nome)

    notas = []
    while True:
        nota = float(input("Digite uma nota de 0 a 10:"))

        if nota >= 0 and nota <= 10:
            notas.append(nota)
        else:
            print("Digite uma nota válida...")

        if len(notas) >= 4:
            print("Cadastro de notas encerrado...")
            break
    
    novoAluno.append(notas)
    alunos.append(novoAluno)

print("LISTA DE ALUNOS: ")
contador = 0
for aluno in alunos:

    media = sum(aluno[1])/len(aluno[1])

    situacao = "DESCONHECIDO"
    if media >= 7 and media <= 10:
        situacao = "APROVADO"
    elif media >= 4 and media < 7:
        situacao = "RECUPERAÇÃO"
    elif media >= 0 and media < 4:
        situacao = "REPROVADO"
    else:
        situacao = "ERRO DE CATEGORIZAÇÃO"


    # print(f"{contador+1}. {aluno[0]} - {aluno[1]} - {media} - {situacao}")

    notas = aluno[1]
    print(f'''
------- ALUNO {contador+1} -------

Nome: {aluno[0]}
''')
    num_nota = 0
    for nota in aluno[1]:
        print(f"Nota {num_nota+1}: {nota}")
        num_nota+=1

    print('''
----------------------------------
''')


    contador += 1