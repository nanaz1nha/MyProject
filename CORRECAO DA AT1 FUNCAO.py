# CORREÇÃO DA T1 DE FUNCÃO - IDADE
def menor():
    print("Eis, os programas ideias para você:")
    print("Teletubies, Tom e Jerry, Xou da Xuxa...")
    print("se passar das 22h, vai mimir!")
    return
def maior():
    print("Eis, boas opções de carros para vc comprar:")
    print("fiat 147, VW fusca, chevette...")

print("Digite a sua idade:")
idade = int(input())

if idade < 18:
    menor()
else:
    maior()