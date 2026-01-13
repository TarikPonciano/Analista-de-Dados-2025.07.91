import json

#Carregar dados de um JSON

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]

# 1. Exibir a lista de alunos contendo Nome | Mensalidade R$ | Tipo de Plano | Frequência

print("Lista de Alunos:")
print("Nome | Mensalidade R$ | Tipo de Plano | Frequência")
for aluno in lista_alunos:
    print(f"{aluno["nome"]} | {aluno["mensalidade"]} | {aluno["plano"]} | {aluno["frequencia_mensal"]}")


print()
print("--------- RESUMO ---------")
# 2. Exibir total de receita da academia
total_receita = 0
for aluno in lista_alunos:
    total_receita += aluno["mensalidade"]

print(f"Receita Total Mensal: R$ {total_receita:.2f}")

# 3. Exibir a média de idade dos alunos da academia
total_idade = 0

for aluno in lista_alunos:
    total_idade += aluno["idade"]
    
media_idade = total_idade/len(lista_alunos)
print(f"Idade Média dos Alunos: {int(round(media_idade,0))}")

# 4. Frequência total por tipo de plano da academia
total_frequencia = 0

frequencia_por_plano = {

}

for aluno in lista_alunos:

    if aluno["plano"] not in frequencia_por_plano:
        frequencia_por_plano[aluno["plano"]] = 0

    frequencia_por_plano[aluno["plano"]] += aluno["frequencia_mensal"]
    total_frequencia += aluno["frequencia_mensal"]

for plano in frequencia_por_plano:

    print(f"{plano} - {frequencia_por_plano[plano]} - {round((frequencia_por_plano[plano]/total_frequencia)*100, 1)}%")
