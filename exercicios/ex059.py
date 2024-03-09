from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
esc = 0
while esc != 5:
    esc = int(input('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Encerrar programa

    Escolha uma das opções acima:  '''))
    if esc == 1:
        print(f' A soma de {n1} e {n2} é igual a {n1 + n2}.')
    elif esc == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}.')
    elif esc == 3:
        print('O maior número é ', end='') 
        print(n1 if n1 > n2 else n2)
    elif esc == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif esc == 5:
        print('Terminando programa...')
    else:
        print('Opção inválida. Digite novamente: ')
    print('=+' * 20)
    sleep(1.5)
print('Fim do programa.')
print('=+' * 20)
