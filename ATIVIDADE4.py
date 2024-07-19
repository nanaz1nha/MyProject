# Construa um programa onde o usuário digitará as funções que ele pode exercer em um jogo de futebol. Se a resposta for "goleiro", "zagueiro" ou "lateral", exibir "Defesa"; se a resposta for "volante" ou "meia", exibir "Meio-Campo";  se a resposta for "ponta", "atacante ou "centroavante", exibir "Ataque!". Para qualquer outra resposta, exibir "Teimoso".
posicao = input("Digite a função de campo do jogador:")

if posicao == "goleiro" or posicao == "zagueiro" or posicao == "lateral":
    print("Defesa")
elif posicao == "volante" or posicao == "meia":
    print("Meio-Campo!")
elif posicao == "ponta" or posicao == "atacante" or posicao == "centroavante":
    print("Ataque!")
else:
    print("Teimoso!")