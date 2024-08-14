#Demonstração de métodos em listas.

inss = ["Maria", "Manoel", "José", "Isabela"]
print("Eis, a fila do INSS: ", inss)

novo = input("Insira mais uma pessoa: ")
inss.append(novo)
print("Conferindo a nova lista: ", inss)

print("Vou tirar a última pessoa dessa lista...")
especial = inss.pop()

print("Agora, vou colocá-la na frente de todos!")
inss.insert(0,especial)
print("Conferindo a lista: ", inss)

print("Maria não gostou e reclamou..")
inss.remove("Maria")
print("E agora ela saiu 'pê da vida'", inss)

print("Para não ter mais reclamações, vamos atender... ")
inss.sort()
print("...em ordem alfabética:", inss)

print(f"Onde está esta nova pessoa chamada {especial}? ")
print("Ela agora ficou na posição", inss.index(especial)+1,"!")