#Dicionários

dic = {}

for i in range(3):
    nome = str(input("Digite o nome do aluno: "))
    nota = float(input("Digite a nota do aluno: "))
    dic[nome] = nota

cont = 0
soma = 0
for nome in dic:
    soma += dic[nome]
    cont += 1

media = soma / cont

print(f"Media das notas dos alunos: {round(media, 1)}")