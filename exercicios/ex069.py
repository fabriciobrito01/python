maior = homem = mulher =  m20 = 0
sexo = ' '
while True:
    idade = int(input('Idade: '))
    if idade >= 18:
        maior += 1
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()
        if sexo == 'M':
            sexo = homem
            homem += 1
        elif sexo == 'F' and idade < 20:
            sexo = mulher
            m20 += 1
        esc = str(input('Deseja continuar [S/N]? ')).strip().upper()
    if esc != 'S':
        break
print(f'Foram cadastrados {maior} adultos, {homem} homens e {m20} mulheres abaixo dos 20 anos.')