#Escreva um algoritmo para cadastrar o time e a sua posição na tabela de classificação do campeonato brasileiro. A partir da sua posição, ele deverá exibir as seguintes classificações: "Campeão" (1o. Lugar), "Libertadores!"(entre 1o e 6o.) , "Sul-Americana" (entre 7o. e o 12o.) e "Rebaixado" (entre os 4 últimos). Para clubes que estão entre a 13a. e a 16a. posição...
time = input("Digite o nome do time:")
posicao = int(input("Digite a posição do time na tabela:"))

if not time or not posicao:
    print("Você precisa dizer qual o time e qual a posição dele!")
else:
    if posicao == 1:
        print("Parabéns! Seu time é campeão!")
    elif posicao >= 2 and posicao <=6:
        print("Libertadores!")
    elif posicao >=7 and posicao <=12:
        print("Sul-Americana!")
    elif posicao >=13 and posicao >= 16:
        print("Sem classificação!")
    elif posicao >=17 and posicao >= 20:
        print("Rebaixado!")

    else:
        print("Ação não reconhecida...")