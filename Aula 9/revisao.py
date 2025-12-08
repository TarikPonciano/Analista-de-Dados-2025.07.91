# Crie um programa que pede o preço de 5 produtos válidos e exibe o total. Aceite apenas produtos em que o preço informado está entre 10 reais e 100 reais.

qtd_produtos = 0
soma = 0
while qtd_produtos < 5:
    preco = float(input(f"Digite o preço do produto {qtd_produtos+1}:"))
    if (preco >= 10 and preco <= 100):
        soma += preco
        qtd_produtos += 1
    else:
        print("DIGITE UM PREÇO VÁLIDO!")

print(f"O total dessa compra será: R$ {soma:.2f}")