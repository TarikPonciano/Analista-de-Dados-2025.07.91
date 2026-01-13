nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

nota3 = float(input("Digite a terceira nota: "))

soma = nota1 + nota2 + nota3
media = soma / 3

print(f"A média das notas é: {media:.2f}")

if media >= 7:
    print("O aluno está aprovado!")
else:
    print("O aluno está reprovado!")

