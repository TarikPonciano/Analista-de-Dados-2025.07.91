# https://kmee.github.io/treinamento-python/google/dict-and-files.html

# https://www.w3schools.com/python/python_dictionaries.asp

paciente = {
    "id": 1234,
    "nome": "Bilu",
    "especie": "Cachorro",
    "raça": "SRD",
    "diagnosticos": ["Sarna", "Lichmaniose", "Doença do Carrapato", "Triste"]
}

paciente["cor"] = "Caramelo"
paciente["nome"] = "Pingo"

print("Informações do Paciente:")

# Método dinâmico
for chave in paciente:
    if chave == "diagnosticos":
        print("Lista de Doenças: ")
        contador = 1
        for doenca in paciente[chave]:
            print(f"{contador}. {doenca}")
            contador += 1

    else:
        print(f"{chave.upper()}: {paciente[chave]}")


# Percorrer Valores

# for valor in paciente.values():
#     print(valor)

# Percorrer Chaves

# for chave in paciente.keys():
#     print(chave)

# Percorrer itens
# for chave, valor in paciente.items():
#     print(f"{chave}: {valor}")



# Método clássico
# print(f"ID: {paciente['id']}")
# print(f"NOME: {paciente['nome']}")
# print(f"ESPÉCIE: {paciente['especie']}")
# print(f"RAÇA: {paciente['raça']}")
# print(f"COR: {paciente['cor']}")
# print(f"LISTA DE DIAGNÓSTICOS:")

# contador = 1
# for doenca in paciente["diagnosticos"]:
#     print(f"{contador}. {doenca}")
#     contador += 1
