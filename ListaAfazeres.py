afazeres = []

for i in range(0,5):
    afazeres.append(input("Digite uma tarefa: "))

for x in range(0,5):
    print(f"A {x+1}° tarefa foi executada? (S/N)")
    statusTarefa = input()
    if statusTarefa == "S" or statusTarefa == "s":
        