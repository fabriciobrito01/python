
v = 0
mais = True
while mais:
    mais = False
    sn = 'S'
    #OPÇÃO
    tes = True
    while tes:
        tes = False
        print('CARDÁPIO'.center(30, '='))
        esc = int(input('''
    [ 1 ] COMIDAS
    [ 2 ] BEBIDAS

    O que deseja escolher? '''))
        if esc != 1 and esc != 2:
            print('Opção inválida, digite novamente.')
            tes = True


    #MENU COMIDAS
    if esc ==  1:
        while sn == 'S':
            print('COMIDAS'.center(30, '='))
            com = int(input('''
    [ 1 ] Hambúrguer...............R$12,00
    [ 2 ] Batata frita...............R$8,50
    [ 3 ] Cachorro-quente...............R$11,00

    O que deseja adicionar ao carrinho? '''))
            if com == 1:
                v += 12
            elif com == 2:
                v += 8.50
            elif com == 3:
                v += 11
            else:
                print('Opção inválida, digite novamente.')
            sn = str(input('Deseja adicionar outro item deste menu ao carrinho? [S/N]')).upper()
            print(f'Total a pagar: R${v}')

    #MENU COMIDAS
    if esc == 2:
        while sn == 'S':
            print('BEBIDAS'.center(30, '='))
            beb = int(input('''
    [ 1 ] Refrigerante...............R$6,00
    [ 2 ] Suco natural...............R$5,00
    [ 3 ] Água mineral...............R$2,50

    O que deseja adicionar ao carrinho? '''))
            if beb == 1:
                v += 6
            elif beb == 2:
                v += 5
            elif beb == 3:
                v += 2.50
            else:
                print('Opção inválida, digite novamente.')
            sn = str(input('Deseja adicionar outro item deste menu ao carrinho? [S/N]')).upper()
            print(f'Total a pagar: R${v}')
    mais = True if (input('Deseja mais coisas? [S/N]')).upper() == 'S' else False