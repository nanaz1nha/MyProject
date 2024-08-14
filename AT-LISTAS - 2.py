# Construa um programa que permita a criação de uma lista de afazeres, totalizando a descrição de 5 tarefas diferentes. A seguir, o programa irá perguntar se a primeira tarefa já foi executada. Se sim, o programa deverá excluí-la, além de dar a opção de cadastrar uma nova tarefa.

tarefas = []
for i in range(0,5):
    tarefas.append(input("Digite uma tarefa: "))

for x in range(0,5):
    print(f"A {x+1}° tarefa foi executada? (S/N)")
    statusTarefa = input()
    if statusTarefa == "S" or statusTarefa == "Sim":
        statusTarefa.remove(input("tarefa finalizada!", tarefas))
        tarefas.append(input("Adicione uma nova tarefa!", tarefas))
    elif statusTarefa == "N" or statusTarefa == "Não":
        print("Vá agora fazer suas tarefas!")