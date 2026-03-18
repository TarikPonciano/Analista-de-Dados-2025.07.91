import requests
import pandas as pd

# Faça uma requisição da api do IMDB e crie uma tabela com os 50 melhores filmes de todos os tempos de um gênero a sua escolha. Guarde os resultados em uma tabela excel que contenha Titulo, Ano Lançamento, Nota do Filme, Quantidade de Votos

respostas = requests.get("https://api.imdbapi.dev/titles")

listaFilmes = respostas.json()["titles"]

colecaoFilmes = []

for filme in listaFilmes:
    nome = filme["primaryTitle"]
    anoLancamento = filme["startYear"]

    dadosFilme = {
        "nome": nome,
        "ano": anoLancamento
    }

    colecaoFilmes.append(dadosFilme)

    print(f'{nome} - {anoLancamento}')