from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
h = hypot(co, ca)
print(f'O valor da hipotenusa é {h:.2f}')
'''from math import sqrt
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('qual o conmprimento do cateto adjacente? '))
h = sqrt(co**2+ca**2)
print(f'A hipotenusa vale {h:.2f}')'''