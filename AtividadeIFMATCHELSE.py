# Construa um programa onde o usuário digitará o dia da da semana e o program irá recomendar atividades para esse dia.
print("Digite um dia da semana para fazer uma atividade:")
print("1. Sexta-feira")
print("2. Sábado")
print("3. Domingo")

DiaEscolhido = int(input())
match DiaEscolhido:
    case 1:
       print("Na sexta-feira, teremos um incrível passeio por Penedo!") 
    case 2:
        print("No sábado, iremos fazer um passeio excelente por Petrópolis!")
    case 3:
        print("No domingo, iremos fazer um passeio pela Quinta da Boa Vista!")
    case _:
        print("Opção não reconhecida!")
