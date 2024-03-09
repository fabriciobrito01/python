lista = ('Refrigerante', 5, 'Suco', 3.50, 'Água', 3, 'Salgado', 4, 'Picolé', 4.50, 'Bolo', 18)
print('-' * 50)
print('TABELA DE PREÇOS'.center(50))
print('-' * 50)

print(f'''
{lista[0]}{'.'*30}R${lista[1]:.2f}
{lista[2]}{'.'*30}R${lista[3]:.2f}
{lista[4]}{'.'*30}R${lista[5]:.2f}
{lista[6]}{'.'*30}R${lista[7]:.2f}
{lista[8]}{'.'*30}R${lista[9]:.2f}
{lista[10]}{'.'*30}R${lista[11]:.2f}
''')

print('-' * 50)