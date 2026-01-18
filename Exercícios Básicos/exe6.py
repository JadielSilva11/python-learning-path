idade = int(input("Digite sua idade: "))

if(idade < 0):
    print("Idade invalida!\n")
elif(idade > 0) and (idade <= 12):
    print("Criança!\n")
elif(idade > 12) and (idade <=17):
    print("Adolescente!\n")
else:
    print("Adulto!\n")