# 1 - Crie um programa de cálculo de total de venda. Peça o valor de 5 produtos diferentes (somente o preço) e a quantidade comprada. Ao final exiba o valor total da compra.
# Bônus: Peça o nome dos produtos e ao final exiba a nota fiscal da compra contendo Produto - Preço - Quantidade - Total da Venda

print("Cálculo de Venda - Produtos XYZ")

valor_total = 0

# numero_produtos = int(input("Quantas vendas deseja registrar?"))
historico = ""

for i in range(3):
    nome = input(f"Digite o nome do produto {i+1}:")
    preco = float(input(f"Digite o preço de {nome}: "))
    quantidade = int(input("Digite quantas unidades foram compradas: "))
    valor_venda = preco * quantidade
    valor_total += valor_venda

    print("Venda atual:")
    print(f"{nome} - R$ {preco:.2f} - {quantidade} - R$ {valor_venda:.2f}")

    historico += f"{nome} - R$ {preco:.2f} - {quantidade} - R$ {valor_venda:.2f}\n"

    print(f"Total atual: R$ {valor_total:.2f}")

    # print("Deseja continuar?")
    # resposta = input("Sim ou Não?")
    # if resposta == "Não":
    #     break

print("-------- VENDA FINALIZADA ---------")

print(historico)
print(f"Total final: R$ {valor_total:.2f}")

