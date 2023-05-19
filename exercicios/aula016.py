lanche = ('Suco', 'Salgado', 'Guaravita', 'Bolo')
#TUPLAS SÃO IMUTÁVEIS
#for c in lanche:
    #print(f'Vou comprar {c}')

#for c in range(0, len(lanche)):
    #print(f'Vou comprar {lanche[c]}')

for pos, c in enumerate(lanche):
    print(f'Vou comer {c} na posição {pos}')