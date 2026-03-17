import requests

cep = input("Digite o seu cep: ")

url = f"https://viacep.com.br/ws/{cep}/json"

resposta = requests.get(url)

informacoes = resposta.json()

print(f'''
Informações do seu endereço:
      Logradouro - {informacoes["logradouro"]}
      Cidade - {informacoes["localidade"]}
      UF - {informacoes["uf"]}
      Região - {informacoes["regiao"]}
''')

# print(informacoes)

# print(informacoes["localidade"])

# # Tente construir uma requisição usando o CEP do Senac Centro (60015-000). Imprima no terminal o logradouro, a cidade, o estado e a região desse CEP.

# print(informacoes["estado"])
# print(informacoes["uf"])