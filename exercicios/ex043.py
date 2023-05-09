peso = float(input('Qual seu peso(kg)? '))
alt = float(input('Qual a sua altura(m)? '))
imc = peso / (alt ** 2)
print(f'Seu imc é {imc:.1f}')
if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif 18.5 < imc <= 25:
    print('Você está no seu PESO IDEAL.')
elif 25 < imc <= 30:
    print('Você está em SOBREPESO.')
elif 30 < imc <= 40:
    print('Você está em OBESIDADE.')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA.')
