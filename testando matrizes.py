# demonstração de matrizes em python...
print("eis,a tabela numérica original")
tabuada = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
multiplicar = int(input("Digite o multiplicador:"))

for x in range(0,3):
    for y in range(0,3):
        tabuada [x][y] = tabuada [x][y] * multiplicar

print("eis, o multiplicador: ", multiplicar)
print ("confira o resultado das operações")
for resultado in tabuada:
    print(resultado)