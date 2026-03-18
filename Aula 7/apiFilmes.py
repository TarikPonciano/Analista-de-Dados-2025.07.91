# Exiba no terminal a lista de títulos do site IMDB
# https://api.imdbapi.dev/titles

# Exiba no terminal o nome e a nota do primeiro título
import requests


# resposta = requests.get("https://api.imdbapi.dev/titles")

# primeiroFilme = resposta.json()["titles"][0]

# respostaCompleta = requests.get(f"https://api.imdbapi.dev/titles/{primeiroFilme["id"]}")

# print(respostaCompleta.json())

# Utilizando a ferramenta presente em https://imdbapi.dev/, monte uma requisição que exibe na tela o nome e a nota dos 50 melhores filmes de todos os tempos.

resposta = requests.get("https://api.imdbapi.dev/titles?types=MOVIE&minVoteCount=100000&sortBy=SORT_BY_USER_RATING&sortOrder=DESC")

listaFilmes = resposta.json()["titles"]

for i, filme in enumerate(listaFilmes):

    idFilme = filme["id"]
    nome = filme["primaryTitle"]
    nota = filme["rating"]["aggregateRating"]
    anoLancamento = filme["startYear"]
    generoPrincipal = filme["genres"][0]

    print(f"{i+1}. {nome} | {nota} | {anoLancamento} | {generoPrincipal}")

# Usando pandas transforme essa lista de 50 filmes em uma tabela do excel