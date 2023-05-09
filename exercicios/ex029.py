v = int(input('Qual velocidade do carro em km/h? '))
print(f'Você será multado em R${(v - 80) * 7}.' if v>80 else 'Você está no limite.')