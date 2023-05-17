maior = homem =  m20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        m20 += 1
    esc = ' '
    while esc not in 'SN':
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'Foram cadastrados {maior} adultos, {homem} homens e {m20} mulheres abaixo dos 20 anos.')