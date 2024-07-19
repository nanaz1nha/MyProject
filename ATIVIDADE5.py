# Escreva um algoritmo para criar um sistema de avaliação de serviços prestados, para 5 notas diferentes e informar os seus respectivos valores: "1) péssimo"; "2) ruim"; "3) razoável"; "4) bom" e "5) ótimo". Porém, estas avaliações só poderão ser feitas se o serviço em questão ter sido realmente prestado, atendendo a todos os requisitos. Caso contrário, o usuário deverá digitar "0) não executado", para que o sistema lhe possibilite descrever as suas reclamações.

# captação de feedback de serviço prestado
print("Boa tarde! O serviço foi realizado?")
print("0. Não foi executado.")
print("1. Sim. Foi executado.")
resposta = int(input())

# Captação de avaliação de serviço prestado

if resposta == 1:
    print("Como você avalia os serviços prestados?")
    print("1. péssimo")
    print("2. ruim")
    print("3. razoável")
    print("4. bom")
    print("5. ótimo")
    avaliacao = int(input())
    print("obrigado por nos avaliar!")
elif resposta == 0:
    input("Descreva sua reclamação:")
    print("Pedimos desculpas pelo mal entendido!")
else:
    print("Opção desconhecida!")
