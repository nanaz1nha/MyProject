#Construa um programa onde o usuário digitará quatro notas trimestrais e o programa irá calcular a média
n1 = float(input("Digite o valor da nota 1:"))
n2 = float(input("Digite o valor da nota 2:"))
n3 = float(input("Digite o valor da nota 3:"))
n4 = float(input("Digite o valor da nota 4:"))

soma = n1 + n2 + n3 + n4
media = soma / 4

print(f"A soma é {soma}")
print(f"A média é {media}")
print(type(media))

if media >= 6:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")


