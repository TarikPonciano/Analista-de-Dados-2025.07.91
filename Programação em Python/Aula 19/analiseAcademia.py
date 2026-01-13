import json

#Carregar dados de um JSON

with open("baseAcademia.json","r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

lista_alunos = dados["alunos"]

# 1. Exibir a lista de alunos contendo Nome | Mensalidade R$ | Tipo de Plano | Frequência

# 2. Exibir total de mensalidade por mês da academia
# 3. Exibir a média de idade dos alunos da academia
# 4. Frequência total por tipo de plano da academia