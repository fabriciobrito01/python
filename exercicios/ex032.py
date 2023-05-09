ano = int(input('Digite o ano em que estamos: '))
print(f'{ano} é um ano bissexto.'if ano // 4 == ano / 4 else f'{ano} não é um ano bissexto.')