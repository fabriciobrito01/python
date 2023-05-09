from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nasc
if idade <= 9:
    print(f'O atleta de {idade} anos disputa a categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'O atlteta de {idade} anos disputa a categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'O atleta de {idade} anos disputa a categoria JUNIOR.')
elif 19 < idade <= 25:
    print(f'O atleta de {idade} anos disputa a categoria SÊNIOR.')
elif idade > 26:
    print(f'O atleta de {idade} anos disputa a categoria MASTER.')