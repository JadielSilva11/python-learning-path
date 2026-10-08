class Aluno:
  def __init__(self, nota1, nota2):
    self.nota1 = nota1
    self.nota2 = nota2

  def media(self):
    m = (self.nota1 + self.nota2) / 2
    return m

  def exibir_dados(self, media):
    print("Nota 1: ", self.nota1)
    print("Nota 2: ", self.nota2)
    print("Media: ", media)

  def resultado(self, media):
    if (media > 6):
      print("Aprovado!\n")
    else:
      print("Reprovado!\n")

aluno1 = Aluno(6.0, 7.5)
m = aluno1.media()
aluno1.exibir_dados(m)
aluno1.resultado(m)