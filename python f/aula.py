class Aluno:
    def __init__(self, nome):
        self.nome = nome 
        self.notas = 0
        self.media = 0

    def verifica_notas(self):
        if self.media >= 6:
            print(f'O aluno {self.nome} atingiu uma média de {self.media} pontos e está aprovado.')
        else:
            print(f'O aluno {self.nome} ficou com uma média de {self.media} pontos e está reprovado')


aluno1 = Aluno('João')
aluno2 = Aluno('Gabriel')

aluno1.notas = [5, 6, 8, 9]
aluno1.media = (sum(aluno1.notas) / 4)
aluno1.verifica_notas()

aluno2.notas = [3, 4, 7, 5]
aluno2.media = (sum(aluno2.notas) / 4)
aluno2.verifica_notas()


