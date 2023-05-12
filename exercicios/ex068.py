from random import randint
msg = ('Vamos jogar par ou ímpar! Digite um número: ')
v = 0
while True:
    jog = (int(input(msg)))
    pc = randint(0, 10)
    s = jog + pc
    p_i = ' '
    while p_i not in 'PI':
        p_i = str(input('Par ou Ímpar [P/I]? ')).strip().upper()
    print(f'Você jogou {jog} e o computador {pc} o total foi {s}')
    print('Deu par.' if s % 2 == 0 else 'deu impar')
    if p_i == 'P':
        if s % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu! GAME OVER.')
            break

    elif p_i == 'I':
        if s % 2 != 0:
            print( 'Você venceu!')
            v += 1
        else:
            print('Você perdeu! GAME OVER.')
            break

    else:
        print('Jogada inválida. Jogue novamente.')

print(f'Você conseguiu chegar em {v} vitórias.')
