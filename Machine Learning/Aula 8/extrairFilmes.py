# https://api.imdbapi.dev/titles

import requests
import pandas as pd

resposta = requests.get("https://api.imdbapi.dev/titles?types=MOVIE&minVoteCount=100000&sortBy=SORT_BY_USER_RATING&sortOrder=DESC")

listaFilmes = resposta.json()["titles"]

colecaoFilmes = []

for i, filme in enumerate(listaFilmes):

    idFilme = filme["id"]
    nome = filme["primaryTitle"]
    nota = filme["rating"]["aggregateRating"]
    anoLancamento = filme["startYear"]
    generoPrincipal = filme["genres"][0]

    dadosFilme = {
        "id": idFilme,
        "titulo": nome,
        "nota": nota,
        "ano": anoLancamento,
        "genero": generoPrincipal
    }

    colecaoFilmes.append(dadosFilme)

    print(f"{i+1}. {nome} | {nota} | {anoLancamento} | {generoPrincipal}")

# Usando pandas transforme essa lista de 50 filmes em uma tabela do excel

print(colecaoFilmes)

tabelaFilmes = pd.DataFrame(colecaoFilmes)

mediaGenero = tabelaFilmes.groupby("genero").agg(
    media_genero=("nota", "mean"),
    qtd_filmes=("id", "count")
)

print(mediaGenero)


# tabelaFilmes.to_excel("tabela_filmes.xlsx", index=False)