#Listas

lista = [0] * 5

for i in range(5):
    lista[i] = int(input("> "))

soma = 0
for i in range(5):
    soma += lista[i]

print(f"\nElementos da lista: {lista}\n")
print(f"Soma dos elementos da lista: {soma}\n")
