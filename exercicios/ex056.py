si = 0
hv = 0
nv = ''
mn = 0
for c in range(1, 5):
    print('-='*20)
    nome = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª pessoa [M/F]: '))
    si += idade
    if c == 1 and sexo in 'Mm':
        hv = idade
        nv = nome
    if sexo in 'Mm' and idade > hv:
        hv = idade
        nv = nome
    if sexo in 'Ff' and idade < 20:
        mn += 1

mi = si /4
print(f'A média de idade do grupo é de {mi:.1f} anos.')
print(f'O homem mais velho do grupo tem {hv} anos e se chama {nv}.')
print(f'O grupo tem {mn} mulheres com menos de 20 anos.')