#Comparando duas listas de valores

#lista definida pelo programa
gabarito = ["B", "C", "A", "E", "D"]
#inicializando lista de valores que serão inseridos pelo usuário
respostaUsuario = []
#variável para contabilizar os acertos
acerto = 0
#variável para contabilizar os erros
erro = 0

#loop para receber os valores do usuário
for i in range(0,5):
    #adicionando os valores na lista através do método append
    respostaUsuario.append(input("Informe as letras assinaladas em cada questão: "))
  
#loop para comparar os valores das listas
for i in range(0,5):
    #comparando os valores de acordo com a posição do indice i
    if gabarito[i] == respostaUsuario[i]:
        #contabilizando acertos
        acerto = acerto +1
    else:
        #contabilizando erros
        erro = erro + 1

#imprimindo o resultado de ambos erros e acertos para o usuário.
print(f"A quantidade de acertos foi: {acerto}, e, a quantidade de erros foi: {erro}.")



