#Funções

def receber_valores():
    tempo = float(input("Digite o tempo de duração da viagem: "))
    v_media = float(input("Digite a velocidade media na viagem: "))

    return tempo, v_media

def calcular_distancia(t, v):
    distancia = t * v

    return distancia

def calcular_litros(d):
    litros = d / 12

    return litros

def exibir_valores(t, v, d, l):
    print(f"Distância total percorrida: {d}km")
    print(f"Duração da viagem: {t}h")
    print(f"Velocidade media da viagem: {v}km/h")
    print(f"Quantidade de combustível gasto: {l}litros")

t, v = receber_valores()
d = calcular_distancia(t, v)
l = calcular_litros(d)
exibir_valores(t, v, d, l)