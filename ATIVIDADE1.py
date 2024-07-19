# Construa uma página onde o usuário digitará duas notas escolares. Caso a  média seja abaixo de 4, o programa escreverá "Aluno reprovado". Caso a nota seja maior que 6, escreverá: "Aluno aprovado direto". E no caso em que a nota for maior que 4 e menor que 6 escreverá: "aluno em recuperação". No último caso, o programa deve solicitar a nota de recuperação. Caso ela seja menor que 5, escrever "Reprovado na recuperação" ou, caso contrário, escrever "Aprovado na recuperação"
n1 = float(input("Digite o valor da nota 1:"))
n2 = float(input("Digite o valor da nota 2:"))
media = (n1 + n2 ) / 4

print(f"A média é {media}")


if media >= 6:
    print("Aluno aprovado direto")
elif media <= 4 and media < 6:
    print("Aluno reprovado")
else:
    print("aluno em recuperação")

nota3 = float(input("Digite a nota da prova de recuperação:"))

if nota3 <= 5:
    print("Reprovado na recuperação")
else:
    print("Aprovado na recuperação")

