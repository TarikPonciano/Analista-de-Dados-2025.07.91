# Criar um programa de cálculo de desconto. O programa deverá receber o valor da compra, a idade do cliente e a cidade do cliente. Ao final o programa deverá exibir o valor do desconto aplicado na compra e o novo valor atualizado. Os critérios de desconto são:

#1: Se o cliente tiver mais que 30 anos de idade - Aplicar 5% de desconto

#2: Se o cliente for da cidade Fortaleza - Aplicar 5% de desconto
#   Se o cliente for da cidade Maranguape - Aplicar 10% de desconto
#   Se o cliente for da cidade Morada Nova - Aplicar 20% de desconto

#3: Se o valor total da compra superar 1000 - Aplicar 10% de desconto
#   Se o valor total da compra superar 2000 - Aplicar 15% de desconto

# Os descontos devem ser acumulativos e será a soma dos descontos aplicados.

print("Sistema de Vendas Loja XYZ")

print("Forneça as informações abaixo para calcular o desconto da venda!")

idade_cliente = int(input("Digite a idade do cliente: "))

cidade_cliente = str(input("Digite a cidade do cliente: ")).lower()

valor_venda = float(input("Digite o valor da venda: "))

desconto_venda = 0

if idade_cliente >= 30:
    print("Desconto de idade concedido! ✔️")
    desconto_venda += 0.05
else:
    print("Desconto de idade não foi concedido! ❌")

if cidade_cliente == "fortaleza":
    desconto_venda += 0.05
elif cidade_cliente == "maranguape":
    desconto_venda += 0.10
elif cidade_cliente == "morada nova":
    desconto_venda += 0.20


if valor_venda >= 1000 and valor_venda < 2000:
    desconto_venda += 0.10
elif valor_venda >= 2000:
    desconto_venda += 0.20


valor_desconto = valor_venda * desconto_venda

total_venda = valor_venda - valor_desconto

# Aspas triplas permite escrever múltiplas linhas > ''' TEXTO '''
print(f'''
Informações da Venda:
      
      Valor Original: R$ {valor_venda:.2f}
      Desconto Aplicado: {desconto_venda*100}%
      Valor Descontado: R$ {valor_desconto:.2f}
      Valor Líquido: R$ {total_venda:.2f}
''')