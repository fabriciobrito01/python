print('-' * 20)
print('BANCO CVTI'.center(20))
print('-' * 20)

sac = int(input('Digite o valor que deseja sacar: R$'))
tot = sac
totcedula = 0
cedula = 50
while True:
    if tot >= cedula:
        tot -= cedula
        totcedula += 1
    else:
        if totcedula > 0:
            print(f'Total de {totcedula} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totcedula = 0
        if tot == 0:
            break
print('FIM')