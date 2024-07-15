#Construa um programa onde o usuário digitará quatro notas trimestrais e o programa irá calcular a média
x = int(input("Digite o valor da nota 1:"))
y = int(input("Digite o valor da nota 2:"))
z = int(input("Digite o valor da nota 3:"))
w = int(input("Digite o valor da nota 4:"))

soma = x + y + z + w
media = soma / 4

print(f"A soma é {soma}")
print(f"A média é {media}")

if media > 6:
    print("Aluno reprovado")
else:
    print("Aluno aprovado")