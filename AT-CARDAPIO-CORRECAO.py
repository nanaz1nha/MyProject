print("Vamos montar um cardápio personalizado?")
cafe = []
almoco = []
jantar = []

print("Café da manhã:")
for X in range(0,3):
    opcao = input(f"Digite a {X+1} opção:")
    cafe.append(opcao)
    if opcao == "leite" or opcao == "queijo" or opcao == "pão":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas: ", cafe)

print("Almoço:")
for X in range(0,4):
    opcao = input(f"Digite a {X+1} opção:")
    almoco.append(opcao)
    if opcao == "camarão" or opcao == "peixe" or opcao == "ostras":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas: ", almoco)

print("Jantar:")
for X in range(0,4):
    opcao = input(f"Digite a {X+1} opção:")
    jantar.append(opcao)
    if opcao == "camarão" or opcao == "peixe" or opcao == "ostras":
        print("Alimento não recomendado!")
print("Eis, as opções escolhidas: ", jantar)