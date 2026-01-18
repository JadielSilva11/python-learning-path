#Funções

def ler_temperatura():
    tempC = int(input("Digite a temperatura em Celsius: "))
    return tempC

def converter_temp(tempC):
    tempF = (9 * tempC + 160) / 5
    return tempF


c = ler_temperatura()
f = converter_temp(c)

print(f"Temperatura em Celsius: {c}")
print(f"Temperatura em Fahrenheit: {f}")