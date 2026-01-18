#Manipulação de arquivos

dic = {"Jadiel": 8.0, "Maria": 9.0, "João": 7.0}

with open('notas.txt', 'w') as arquivo:
    for nome, nota in dic.items():
        arquivo.write(f"{nome}, {nota}\n")

with open('notas.txt') as arquivo:
    read = arquivo.readlines()

print(read)