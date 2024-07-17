# Programa para converter temperaturas...
print ("Qual conversão você deseja realizar?")
escolha = int(input("1. Celsius / 2. Kelvin / 3. Fahrenheit: "))
temperatura = int(input("Digite o valor da temperatura:"))

match escolha:
    case 1:
        kelvin = temperatura + 273
        fahrenheit = (9 / 5 * temperatura) - 32
        print(f"A conversão de Celsius para Kelvin será {kelvin}")
        print(f"A conversão de Celsius para fahrenheit será {fahrenheit}")
    case 2:
        celsius = temperatura - 273
        fahrenheit = (temperatura - 273) * 1.8 + 32
        print(f"A conversão de kelvin para celsius será {celsius}")
        print(f"A conversão de kelvin para fahrenheit será {fahrenheit}")
    case 3:
        celsius = 5 / 9 * (temperatura - 32)
        kelvin = (temperatura - 32) / 1.8 + 273
        print(f"A conversão de fahrenheit para celsius será {celsius}")
        print(f"A conversão de fahrenheit para kelvin será {kelvin}")

