from math import sin, cos, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
coss = cos(radians(an))
tang = tan(radians(an))
print(f'O seno vale {sen:.2f}, o cosseno vale {coss:.2f} e a tangente vale {tang:.2f}.')
