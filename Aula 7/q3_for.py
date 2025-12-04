# 3 - Crie um programa de cálculo de notas. O programa deverá pedir ao usuário as 4 notas de um aluno (usar for) e ao final deverá exibir média e situação do aluno.
# >= 7 - Aprovado
# >= 4 and < 7 - Recuperação
# < 4 - Reprovado
# Bônus: Peça ao usuário quantas notas ele deseja digitar. Utilize no cálculo de média somente notas válidas (0 a 10). Ao final exiba o boletim do aluno.



num_notas = int(input("Quantas notas serão digitadas?"))

soma = 0
notas_validas = 0
historico = ""

for i in range(num_notas):
    nota = float(input(f"Digite a nota {i+1}:"))
    if nota >= 0 and nota <= 10:
        soma += nota
        notas_validas += 1
        historico += f"Prova {notas_validas} - {nota:.1f}\n"

media = soma/notas_validas
print(f"Média do aluno: {media:.1f}")
print(historico)

situacao = ""

if media >= 7 and media <= 10:
    situacao = "Aprovado"
elif media >= 4 and media < 7:
    situacao = "Recuperação"
elif media < 4 and media >= 0:
    situacao = "Reprovado"
else:
    situacao = "Não foi possível determinar a situação do aluno! Média inválida!"

print(f"Situação do aluno: {situacao}")

