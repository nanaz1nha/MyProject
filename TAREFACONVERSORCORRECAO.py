# Programa para converter temperaturas
print("Converter de Fahrenheit para Celsius e Kelvin...")
fahrenheit = int(input("Digite a temperatura em Fahrenheit:"))
celsius = (fahrenheit - 32) / 1.8
kelvin = (fahrenheit - 32) * 5 / 9 + 273
print(f"A temperatura em celsius será {celsius}.")
print(f"A temperatura em fahrenheit será {kelvin}.")



