# https://servicodados.ibge.gov.br/api/v1/localidades/estados

# Faça uma requisição ao endpoint de estados do IBGE
# A partir do resultado da requisição imprima o nome de todos os estados do Brasil

# Imprima agora para cada estado "Nome - Região"

import requests
import pandas as pd

resposta = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")

listaEstados = resposta.json()

listaEstadosFormatado = []

for estado in listaEstados:
    
    idEstado = estado["id"]
    nome = estado["nome"]
    uf = estado["sigla"]
    regiao = estado["regiao"]["nome"]

    estadoFormatado = {
        "id": idEstado,
        "nome": nome,
        "uf": uf,
        "regiao": regiao
    }

    listaEstadosFormatado.append(estadoFormatado)


df = pd.DataFrame(listaEstadosFormatado)

df = df.sort_values("id", ascending=True)

df.to_excel("tabela_estados.xlsx", index=False)