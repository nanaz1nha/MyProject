#Demonstração funções em listas

print("Os meus maiores sonhos.." )
sonhos = ["1. Viajar o mundo",
          "2. Praia Sepetiba ",
          "3. Férias em Paris", 
          "4. Compras no WestShopping",
          "5. Ver as pirâmides do Egito"]
for x in sonhos: 
    print(x)

print("Ops, não quero Sepetiba!")
del(sonhos[1])
print("E nem WestShopping...")
del(sonhos[2])

print("Conferindo os sonhos... ")
for x in sonhos:
    print(x)
