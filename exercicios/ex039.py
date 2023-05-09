from datetime import date
atual = date.today().year
ano = int(input('Em que ano o candidato nasceu? '))
idade = atual - ano
if idade == 18:
    print('Está na hora do candidato se alistar.')
elif idade < 18:
    print(f'''Ainda não está na hora de se alistar. Faltam {18 - idade} ano(s).
Seu alistamento será em {atual + (18 - idade)}''')
else:
    print(f'''Já se passaram {idade - 18} ano(s) da data do alistamento.
Seu alistamento foi em {atual - (idade - 18)}. ''')