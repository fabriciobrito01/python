from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)
print('''Escolha uma jogada: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
op = int(input('Sua escolha: '))
print(f'O computador jogou {(itens[pc])}.')
print(f'O jogador jogou {(itens[op])}.')
if pc == 0:
    if op == 0:
        print('Empate!')
    elif op == 1:
        print('Você venceu!')
    elif op == 2:
        print('O computador venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 1:
    if op == 0:
        print('O computador venceu!')
    elif op == 1:
        print('Empate!')
    elif op == 2:
        print('Você venceu!')
    else:
        print('JOGADA INVÁLIDA!')
elif pc == 2:
    if op == 0:
        print('Você venceu!')
    elif op == 1:
        print('O computador venceu!')
    elif op == 2:
        print('Empate!')
    else:
        print('JOGADA INVÁLIDA!')