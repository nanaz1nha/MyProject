# DEMONSTRAÇÃO DO USO DE FUNÇÕES....
#essas funções abaixo vão ser guardadas na memória
def adicao(X, Y):
    return X + Y
def subtracao(X,Y):
    return X - Y
def multiplicacao(X,Y):
    return X * Y
def divisao(X,Y):
    return X / Y

#captando os dados para fazer a operação
print("Digite dois valores inteiros...")
n1 = int(input("X: "))
n2 = int(input("Y: "))
op = input("Qual operação (+, - , * ou / )?")

# if irá identificar a operacao 
if op == "+":
    z = adicao(n1, n2)
    print("Resultado da soma:", z)
elif op == "-":
    z = subtracao(n1,n2)
    print("Resultado da subtração:", z)
elif op == "*":
    z = multiplicacao(n1,n2)
    print("Resultado da multiplicação:", z)
elif op == "/":
    z = divisao(n1,n2)
    print("Resultado da divisão:", z)
else:
    print("Opção digitada inexistente!")