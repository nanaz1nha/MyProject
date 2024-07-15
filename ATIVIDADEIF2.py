#Construa um programa onde o usuário digitará quatro notas trimestrais e o programa irá calcular a média
X = float(input("Digite o valor da nota 1:"))
Y = float(input("Digite o valor da nota 2:"))
Z = float(input("Digite o valor da nota 3:"))
W = float(input("Digite o valor da nota 4:"))

soma = X + Y + Z + W
media = soma / 4

print(f"A soma é {soma}")
print(f"A média é {media}")

if media > 6:
print("Aluno reprovado")

else:
print("Aluno aprovado")

