print("Sistema RH XYZ")

print('''
Menu:
      1. Ver Funcionários
      2. Adicionar Funcionário
      3. Ver Folha de Pagamento
      4. Demitir Funcionário
      
      0. Sair
''')

op = input("Digite a opção desejada do menu: ")

if op == "1" or op.lower() == "ver funcionários" or "ver" in op:
    # Código Ver Funcionários aqui
    print("Ver Funcionários ativado!")
elif op == "2" or "adicionar" in op:
    # Código Adicionar Funcionário
    print("Adicionar Funcionário ativado!")
elif op == "0":
    # Saindo
    print("Saindo do Programa...")
    exit()
else:
    print("Digite uma opção válida...")