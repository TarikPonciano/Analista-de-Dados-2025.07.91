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

dados["identificador"] = dados["nome"] + " - " + dados["turma"]

# Produzir a coluna Situação informando a situação de cada aluno

# Aprovado -> 7 a 10
# Recuperação -> 4 a 7
# Reprovado -> 0 a 4

# Atribuição condicional com apply

def classificar_media(nota):
    if nota >= 7 and nota <= 10:
        return "Aprovado"
    elif nota >= 4 and nota < 7:
        return "Recuperação"
    elif nota >= 0 and nota < 4:
        return "Reprovado"
    else:
        return "MÉDIA INVÁLIDA"
    

dados["situacao"] = dados["media"].apply(classificar_media)

# Método usando loc

# dados["situacao"] = "Reprovado"

# dados.loc[(dados["media"] >= 4) & (dados["media"] < 7), "situacao"] = "Recuperação"

# dados.loc[(dados["media"] >= 7) & (dados["media"] <= 10), "situacao"] = "Aprovado"

# Exibir 3 seções distintas. Tabela para aprovados, tabela para reprovados e tabela para recuperação

#Lista de Aprovados
aprovados = dados[dados["situacao"]=="Aprovado"]

print("Lista de Aprovados:")

print(aprovados[["identificador", "media","situacao"]])

#Lista de Recuperação
recuperacao = dados[dados["situacao"]=="Recuperação"]

print("Lista de Recuperação:")

print(recuperacao[["identificador", "media","situacao"]])

#Lista de Recuperação
reprovados = dados[dados["situacao"]=="Reprovado"]

print("Lista de Reprovados:")

print(reprovados[["identificador", "media","situacao"]])

# Mostre os 5 melhores alunos
# Mostre os 5 piores alunos 

dados_ordenado = dados.sort_values("media", ascending=False)

print("TOP 5 Alunos")
print(dados_ordenado[["nome", "media"]].head(5))

print("BOTTOM 5 Alunos")
print(dados_ordenado[["nome","media"]].tail(5))

print(dados["turma"].value_counts())
print(dados["situacao"].value_counts())
print(dados["situacao"].value_counts(normalize=True))
print(dados[["turma", "situacao"]].value_counts())

agrupamento_turma = dados.groupby("turma")

agregados_turma = agrupamento_turma.agg(
    media_b1=("nota_b1", "mean"),
    media_b2=("nota_b2", "mean"),
    media_b3=("nota_b3", "mean"),
    media_b4=("nota_b4", "mean"),
    media_geral=("media", "mean"),
    maior_media=("media", "max"),
    menor_media=("media", "min")
) 
print(agregados_turma)

# dados.to_excel("boletins_enriquecido.xlsx", index=False)