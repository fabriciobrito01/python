from random import choice
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [pa, sa, ta, qa]
s = choice(lista)
print(f'O aluno sorteado foi {s}.')