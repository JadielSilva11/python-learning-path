n1 = float(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))

media = (n1 + n2 + n3) / 3

if(media >= 7.0):
    print("Aprovado!\n")
elif (media > 4.0) and (media < 7):
    print("Você deverá fazer o exame de recuperação!\n")

    exame = int(input("Digite a sua nota do exame: "))
    if (exame < 6.0):
        print("Reprovado!\n")
    else:
        print("Aprovado!\n")
else:
    print("Reprovado!\n")