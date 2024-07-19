# Faça um programa que verifique se um trabalhador está qualificado para se aposentar (ou não).

# Coleta de dados da pessoa
sexo = (input("Digite o sexo do empregado:"))
print("1. Masculino")
print("2. Feminino")
idade = int(input("Digite a idade do empregado:"))
contribuicao = int(input("Digite o tempo de contribuição:"))

if sexo == 2 or sexo == "feminino" and idade <= 62 and contribuicao <= 15:
    print("Você já pode se aposentar")
elif sexo == 1 or sexo == "masculino" and idade <= 65 and contribuicao <= 20:
    print("Você já pode se aposentar!")
elif sexo == 2 or sexo == "feminino"  and contribuicao <= 30:
    print("Você já pode se aposentar")
elif sexo == 1 or sexo == "masculino" and contribuicao <= 35:
    print("Você já pode se aposentar!")
else:
    print("Você ainda vai ter que trabalhar muito!")