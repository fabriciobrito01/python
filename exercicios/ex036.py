v = float(input('Qual o valor da casa? '))
s = float(input('Qual é o seu salário? '))
a = int(input('Em quantos anos você deseja pagar a casa? '))
p = v / a
pm = p / 12
if pm < s - (s * 30 / 100):
    print((f'Você deverá pagar {pm:.2f} por mês durante {a} anos. '), end='')
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado!')