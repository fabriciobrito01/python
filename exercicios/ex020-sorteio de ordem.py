from random import shuffle
pa = input('Primeiro aluno: ')
sa = input('Segundo aluno: ')
ta = input('Terceiro aluno: ')
qa = input('Quarto aluno: ')
lista = [pa, sa, ta, qa]
shuffle(lista)
print(f'A ordem de apresentação será: {lista}.')
