#CONSTRUA UM PROGRAMA ONDE O USUÁRIO DIGITARÁ A SUA IDADE. SE A IDADE FOR MENOR DE 18 ANOS, O PROGRAMA ENTRARÁ EM UMA FUNÇÃO LISTANDO NOMES DE PROGRAMAS INFANTIS. CASO SEJA MAIOR DE IDADE, ENTRARÁ EM UMA OUTRA FUNÇÃO COM LISTA DE CARROS E SEUS RESPECTIVOS PREÇOS.
def conferir(X):
    if X >= 18:
        print("Você é maior de idade! Já pode comprar um carro: 1 - Monza 2 - Fusca 3 - Chevette")
    else:
        print("Ops, menor de idade! Escolha um desenho para assistir: 1 - Padrinhos Mágicos 2 - Tom e Jerry 3 - Hora de Aventura")
    return
#coletando dados
MyAge = int(input("Digite a sua idade: "))

conferir(MyAge)