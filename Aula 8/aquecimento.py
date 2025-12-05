# Crie um programa que recebe a quantidade de candidatos que prestaram uma prova de concurso. Depois disso, para cada candidato, peça o nome e a nota (0 a 100) obtida no concurso, se o candidato tiver obtido nota maior ou igual a 80, imprima na tela "{nome} - Aprovado". Ao final exiba um resumo contendo Total de Aprovados, Total de Reprovados e Média Geral. Bônus: Antes do resumo exiba a lista candidatos com Nome - Nota - Situação.

qtd_candidatos = int(input("Digite a quantidade de candidatos: "))

total_aprovados = 0
total_reprovados = 0
soma_notas = 0
historico = ""

for i in range(qtd_candidatos):
    nome = input(f"Digite o nome do candidato {i+1}:")

    nota = int(input(f"Digite a nota (0-100) do candidato {i+1}:"))

    soma_notas += nota

    #Verificar se foi aprovado e imprimir a mensagem correspondente

    if nota >= 80:
        print(f"Candidato {i+1}: {nome} - Aprovado")
        total_aprovados += 1

        historico += f"{i+1}. {nome} - {nota} - Aprovado\n"
    else:
        print(f"Candidato {i+1}: {nome} - Reprovado")
        total_reprovados += 1
        historico += f"{i+1}. {nome} - {nota} - Reprovado\n"

print("Lista de Participantes:")
print(historico)


print("------------RESUMO DO CONCURSO------------")
print("Aprovados:", total_aprovados)
print("Reprovados:", total_reprovados)
print("Média Geral:", round((soma_notas/qtd_candidatos),2))
# print(f"Média Geral: {round((soma_notas/qtd_candidatos), 2)}")