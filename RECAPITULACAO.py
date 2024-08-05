# Este é um comentário !
name = "Fulaninho"
print(f"Olá, {name} ! Voltamos de férias...")
ferias = int(input("Quantos dias ficamos de férias?"))
print(f"ficamos {ferias} dias de férias")

# recapitulando o uso de condições...
maisferias = int(input("Quantos dias a mais quer de férias?"))
maisferias = maisferias + ferias
print(f"Ok, a partir de agora, terá {maisferias} dias de férias!")

local = input(" ual foi o local que você viajou?")
if local == "Disney":
    print("Então você levou as crianças!")
elif local == "Paris":
    print("Então foi um passeio romântico...")
else:
    pinrt("ok, não conheço esse lugar!")

# recapitulando o uso de match case
    
local = input("Qual foi o local para onde você viajou?")
match local:
    case "disney":
        print("local legal para levar crianças")
    case "Paris":
        print("Lugar perfeito para passeios românticos")
    case _:
        print("num conheço não...")