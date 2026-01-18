#Orientação a objetos

class Aluno:
    def __init__(self, nota1, nota2):
        self.nota1 = nota1
        self.nota2 = nota2

    def media(self):
        media = (self.nota1 + self.nota2) / 2
        return media
    
    def exibir_dados(self, media):
        print(f"Nota 1: {self.nota1}")
        print(f"Nota 2: {self.nota2}")
        print(f"Media: {media}")

    def resultado_final(self,media):
        if(media >= 7.0):
            print("Aprovado!\n")
        else:
            print("Reprovado!\n")

print("Notas, media e resultado final do aluno 1:")
aluno1 = Aluno(8.0, 9.0)
m = aluno1.media()
aluno1.exibir_dados(m)
aluno1.resultado_final(m)

print("Notas, media e resultado final do aluno 2:")
aluno2 = Aluno(3.0, 6.0)
m = aluno2.media()
aluno2.exibir_dados(m)
aluno2.resultado_final(m)