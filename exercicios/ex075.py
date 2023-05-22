n = (int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')))
print(f'''
Os números digitado foram {n};
O número 9 apareceu {n.count(9)} vezes;''')
if 3 in n:
    print(f'O primeiro 3 apareceu na posição {n.index(3) + 1};')
else:
    print('O número 3 não apareceu na tupla.')
print('Os números pares foram ', end='')
for par in n:
    if par % 2 == 0:
        print(par, end=', ')
