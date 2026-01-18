#Input e exibição dinâmica

tempo = float(input("Digite o tempo de duração da viagem em horas: "))
v_media = float(input("Digite a velocidade media durante o percurso em quilometros: "))

distancia = v_media * tempo
litros = distancia / 12

print(f"Distância total da viagem: {round(distancia, 1)}km\nDuração total da viagem: {round(tempo, 1)}h\nVelocidade media: {round(v_media, 1)}km/h\nLitros gastos durante a viagem: {round(litros, 1)}litros\n")