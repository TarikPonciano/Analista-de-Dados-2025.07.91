# pessoa_lista = ["João", 23, 1.7]
dicionario_vazio = {}

pessoa_dicionario = {
    "nome": "João",
    "idade": 23,
    "altura": 1.7
}

# CRUD
# Ler

# Leitura direta
print(pessoa_dicionario["nome"])

print(pessoa_dicionario.get("telefone", "Informação não encontrada"))

# Criar

pessoa_dicionario["telefone"] = "85988942250"

print(pessoa_dicionario)

# Modificar
pessoa_dicionario["nome"] = "Tarik"

print(pessoa_dicionario)

# Remover

pessoa_dicionario.pop("idade")

# del pessoa_dicionario["idade"]

print(pessoa_dicionario)
