# https://servicodados.ibge.gov.br/api/v1/localidades/estados

# Faça uma requisição ao endpoint de estados do IBGE
# A partir do resultado da requisição imprima o nome de todos os estados do Brasil

# Imprima agora para cada estado "Nome - Região"

import requests

resposta = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")

listaEstados = resposta.json()

for estado in listaEstados:
    print(estado["nome"])
