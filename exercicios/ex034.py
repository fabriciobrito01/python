s = float(input('Qual o seu salário? R$ '))
a1 = (s * 10 / 100 + s)
a2 = (s * 15 / 100 + s)
print(f'Seu novo salário será R${a1}' if s > 1250 else f'Seu novo salário será R${a2}.')