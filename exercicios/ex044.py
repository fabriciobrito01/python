v = float(input('Qual o valor do produto? R$'))
print('''ESCOLHA A FORMA DE PAGAMENTO:
[ 1 ] à vista no dinheiro ou cheque. (10% OFF)
[ 2 ] à vista no cartão. (5% OFF)
[ 3 ] em até 2x no cartão.
[ 4 ] 3x ou mais no cartão. (20% J)''')
op = int(input('Digite a forma de pagamento escolhida: '))
if op == 1:
    print(f'O produto de R${v:.2f} custará R${v - (v * 10 / 100):.2f} com 10% de desconto.')
elif op == 2:
    print(f'O produto de R${v:.2f} custará R${v - (v * 5 / 100):.2f} com 5% de desconto.')
elif op == 3:
    p = v / 2
    print(f'O produto de R${v:.2f} será parcelado em 2x de R${p:.2f} no cartão.')
elif op == 4:
    p = (int(input('Em quantas vezes deseja parcelar? ')))
    vj = v + (v * 20 / 100)
    print(f'O produto de R${v:.2f} será parcelado em {p}x de R${vj / p:.2f} com juros')
else:
    print('Opção inválida. Digite novamente.')