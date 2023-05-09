d = int(input('Qual será a distância em km da sua viagem? '))
p1 = (d * 0.50)
p2 = (d * 0.45)
print(f'Você deverá pagar R${p2} de passagem.' if d > 200 else f'Você deverá pagar R${p1}.')