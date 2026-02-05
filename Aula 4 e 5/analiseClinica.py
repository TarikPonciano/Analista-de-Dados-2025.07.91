import pandas as pd

dados = pd.read_excel("dados_clinica_simplificado.xlsx", engine="openpyxl")

# Missão 1 - Diagnóstico dos dados

# print(dados.head(10))

# print("Dimensões")
# print(f"Linhas: {dados.shape[0]} Colunas: {dados.shape[1]}")

# print("Tipos de dados das colunas")
# print(dados.dtypes)

# print("Dados nulos por coluna")
# print(dados.isnull().sum())

# Missão 2 - Padronização dos nomes
dados["Nome"] = dados["Nome"].astype("str").str.strip().str.title()

# Missão 3 - Padronizar idade


dados["Idade"] = dados["Idade"].replace(["", " ", "N/A"], pd.NA)

dados["Idade"] = pd.to_numeric(dados["Idade"], errors="coerce")

# Se a coluna for extremamente importante, faz sentido filtrar os dados ruins

# dados_limpo = dados[dados["Idade"].notna()]

mediana_idade = dados[dados["Idade"].notna()]["Idade"].median()

dados.loc[dados["Idade"].isna(), "Idade"] = mediana_idade

dados["Idade"] = dados["Idade"].astype("int64")

dados["Idade"] = dados["Idade"].clip(lower=0, upper=120)

# print(dados[(dados["Idade"] < 0) | (dados["Idade"] > 120)])


# print(mediana_idade)
print(dados["Sexo"].value_counts())

