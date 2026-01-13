# 1 - Crie um programa de cálculo de total de venda. Peça o valor de 5 produtos diferentes (somente o preço) e a quantidade comprada. Ao final exiba o valor total da compra.
# Bônus: Peça o nome dos produtos e ao final exiba a nota fiscal da compra contendo Produto - Preço - Quantidade - Total

print("Cálculo de Venda - Produtos XYZ")

valor_total = 0

# numero_produtos = int(input("Quantas vendas deseja registrar?"))

for i in range(5):
    preco = float(input(f"Digite o preço do produto {i+1}: "))
    quantidade = int(input("Digite quantas unidades foram compradas: "))
    valor_venda = preco * quantidade
    valor_total += valor_venda

    print(f"Produto de R$ {preco:.2f}")
    print(f"{quantidade} unidades vendidas")
    print(f"Valor dessa venda: R$ {valor_venda:.2f}")
    print(f"Total atual: R$ {valor_total:.2f}")

    # print("Deseja continuar?")
    # resposta = input("Sim ou Não?")
    # if resposta == "Não":
    #     break

print("-------- VENDA FINALIZADA ---------")
print(f"Total final: R$ {valor_total:.2f}")

