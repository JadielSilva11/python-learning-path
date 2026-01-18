#Tratamento de exceções

try:
    lista = []
    for i in range(2):
        num = int(input("Digite um numero: "))
        lista.append(num)
    result = lista[0] / lista[1]
except ValueError:
    print("Não é possível inserir caracteres!\n")
except ZeroDivisionError:
    print("Não é possivel inserir zero no segundo número!\n")
except IndexError:
    print("Está acessando uma posição que não existe na lista!\n")
except KeyboardInterrupt:
    print("Execução cancelada pelo usuário!\n")
else:
    print(f"Divisão de {lista[0]} por {lista[1]} = {lista[0] / lista[1]}")