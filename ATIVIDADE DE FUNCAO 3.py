# CONSTRUA UM PROGRAMA ONDE O USUÁRIO IRÁ DIGITAR SEU NOME E CIDADE DE ONDE ESTÁ DIGITANDO. ESSAS INFORMAÇÕES PASSARÃO PARA UMA FUNÇÃO E, CASO A CIDADE SEJA "RIO DE JANEIRO", A REPOSTA, ALÉM DO NOME DA PESSOA, ESCREVERÁ "SEJA BEM VINDO À CIDADE MARAVILHOSA". CASO CONTRÁRIO, EXIBIRÁ APENAS O NOME E A CIDADE DIGITADA.
def CONFERIR(X):
    if X == "Rio de Janeiro":
        print(f"Olá, {NyName} ! Seja bem vindo à Cidade Maravilhosa!")
    else:
        print(f"Seu nome é {NyName} e vc está digitando de {MyCity} .")
    return
    #coletando dados
NyName = str(input("Digite o seu nome: "))
MyCity = str(input("Digite a sua Cidade de onde você está digitando: "))


CONFERIR(MyCity)