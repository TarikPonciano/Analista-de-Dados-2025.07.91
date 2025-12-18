# 1. Crie um dicionário que representa o produto de um supermercado. Esse produto deve possuir nome, preço e estoque. Imprima ao final as informações desse produto de forma fichada:
#Exemplo:
#Informações do Produto:
# Nome: Banana
# Preço: R$ 1.75
# Estoque: 300

produto = {
    "nome": "Coca Zero 2l",
    "preço": 9.99,
    "estoque": 500
}

print(f'''
Informações do Produto:
      
      Nome: {produto["nome"]}
      Preço: R$ {produto["preço"]:.2f}
      Estoque: {produto["estoque"]}

''')


# 2. Crie um dicionário que organiza os contatos telefônicos de alguém. Como chave você deverá utilizar o nome da pessoa e como valor, o telefone da pessoa. Crie 5 contatos e exiba somente o telefone de um contato chamado "Mario".

# 3. Faça o cadastro de um cliente, peça as informações nome, cpf, idade, gênero e altura e armazene em um dicionário. Ao final imprima as informações de forma fichada.

