# Construa um programa onde o usuário irá digitar 3 números distintos, que por sua vez serão armazenados nas variáveis "X" , "Y" e "Z". A partir daí, o programa informe se estes números estão em ordem crescente ou descrecente. Se não, exibir "Eles estão misturados!"
X = int(input("Digite o primeiro número:"))
Y = int(input("Digite o segundo número:"))
Z = int(input("Digite o terceiro número:"))

if X < Y < Z:
    print("Os números estão em ordem crescente!")
elif X > Y > Z:
    print("Os números estão em ordem decrescente!")
else:
    print("Os números estão misturados!")