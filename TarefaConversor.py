# Faça um programa que faça a conversão da temperatura, em diferetes unidades  de medida: 1 - De Celsius para Kelvin e Fahrenheit ; 2 - De Kelvin para Celsius e Fahrenheit ; 3 De Fahremheit para Celsius e Kelvin.

print(f"Digite a unidade a ser convertida:")
print("1. Celsius")
print("2. Kelvin")
print("3. Fahrenheit")
unidade = str(input())

match unidade:
    case 1:
         


CpK = C + 273
CpF = C * 1,8 + 32
KpC = C - 273
KpF = (K-273) * 1,8 + 32
FpC = (F - 32) / 1,8
FpK = (F - 32) * 5 / 9 + 273

print(f"A conversão de Celsius para Kelvin é:{CpK}")
print(f"A conversão de Celsius para Fahrenheit é:{CpF}")



print(f"A conversão de Kelvin para Celsius é:{KpC}")
print(f"A conversão de Kelvin para Fahrenheit é:{KpF}")



print(f"A conversão de Fahrenheit para Celsius é:{FpC}")
print(f"A conversão de Fahrenheit para Kelvin é:{FpK}")
