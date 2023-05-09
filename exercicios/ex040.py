n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
print(f'O aluno ficou com {m} na média.')
if m < 5.0:
    print('O aluno está reprovado.')
elif 5.0 <= m < 7:
    print('O aluno está de recuperação.')
else:
    print('O aluno está aprovado.')