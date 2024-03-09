tot = maior = menor = c = 0
barato = caro = ' '

print('=' * 20)
print('ATACADÃO'.center(20))
print('=' * 20)

while True:
    produto = str(input('Produto: ')).capitalize().strip()
    preço = float(input('Valor: '))
    tot += preço
    c += 1
    
    if c == 1:
        maior = menor = preço
    
    else:
        if preço > maior:
            maior = preço
            caro = produto
        if preço < menor:
            menor = preço
            barato = produto

    esc = str(input('Deseja adicionar outro produto [S/N]? ')).strip().upper()[0]
    if esc == 'N':
        break
print(f'O preço total da compra foi R${tot}')
print(f'{caro} foi o produto mais caro e custou R${maior}')
print(f'{barato} foi o produto mais barato e custou R${menor}.')
print('COMPRA FINALIZADA')
