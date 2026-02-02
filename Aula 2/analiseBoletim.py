# pip install pandas openpyxl
import pandas as pd


dados = pd.read_excel("boletins.xlsx", engine="openpyxl")

print(dados)

# Produzir coluna média dos alunos

# Maneira manual
# dados.loc[dados["nota_b1"].isnull(), "nota_b1"] = 0
# dados.loc[dados["nota_b2"].isnull(), "nota_b2"] = 0
# dados.loc[dados["nota_b3"].isnull(), "nota_b3"] = 0
# dados.loc[dados["nota_b4"].isnull(), "nota_b4"] = 0

# Maneira funcional
dados[["nota_b1", "nota_b2", "nota_b3", "nota_b4"]] = dados[["nota_b1", "nota_b2", "nota_b3", "nota_b4"]].fillna(0)

# Maneira manual
dados["media"] = (dados["nota_b1"] + dados["nota_b2"] + dados["nota_b3"] + dados["nota_b4"])/4

#Maneira funcional
# dados["media"] = dados[["nota_b1", "nota_b2", "nota_b3", "nota_b4"]].mean(axis=1)

dados["Identificador"] = dados["nome"] + " - " + dados["turma"]

# Produzir a coluna Situação informando a situação de cada aluno



