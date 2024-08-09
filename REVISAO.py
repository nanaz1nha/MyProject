#REVISÃO GERAL DE ALGORITMOS E LÓGICA DE PROGRAMAÇÃO...

# UTILIZANDO O INPUT
print("Digite o seu nome:")
nome = str(input())

# ALTERNATIVA DE USAR O INPUT UTILIZANDO CLASSES: INT, STR E FLOAT:
idade = int(input("Digite a idade:"))
altura = float(input("Digite a altura:"))

# UTILIZAR O FSTRING É UMA ALTERNATIVA MAIS SIMPLES PARA IMPRIMIR DADOS NO TERMINAL
print(f"Meu nome é {nome},")
print(f"a minha idade é {idade},")
print(f"e a minha altura é {altura}.")

#TIPO DE FUNÇÃO QUE IMPRIME O TIPO DE CLASSE QUE É CADA VARIÁVEL
print(type(nome))
print(type(idade))
print(type(altura))

# UTILIZANDO CALCULOS
print("Qual será a minha idade em 2036?")
tempo = 2036 - 2024
idade = idade + tempo
altura = altura / 2
print(f"a minha idade em 2036 será: {idade}")
print(f"A metade da minha altura é:{altura}")
