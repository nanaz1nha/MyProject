print("Vou montar a marmita com 5 elemntos! ")
marmita = ["feijão", "arroz","legumes", "salada", "carne"]
print("Eis, a nossa recomendação: ", marmita)

resposta = input("Você quer montar uma marmita diferente? (S/N)")
if resposta == "S" or resposta  == "s":
    for x in range(0,5):
        print(f"Digite o {x+1}o. item do cardápio: ")
        marmita[x] = input()
    print(f"A marmita montada foi: {marmita}")
    print(f"Os três primeiros itens foram: {marmita[0:3]}" )
    print(f"O último item foi: {marmita[-1]}" )
    print(marmita[:])
    print(marmita[2:3])
    print(marmita[0:4:2])
    print(marmita[-3:-1])
else:
    print("Ok, você decide..")