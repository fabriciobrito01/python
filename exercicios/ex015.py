d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km o veículo percorreu? '))
vd = d * 60
vkm = km * 0.15
vt = vd + vkm
print(f'O valor total é de R${vt:.2f}.')