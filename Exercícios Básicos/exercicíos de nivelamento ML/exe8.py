#Repetições (for)

soma = 0 
i = 1

for i in range(1, 6):
    soma += int(input(f"Digite a nota {i}: "))

media = soma / i
print(f"Sua media é: {media}")