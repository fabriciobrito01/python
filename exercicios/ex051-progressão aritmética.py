print('=+' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('=+' * 20)
n1 = int(input('Digite o primeiro termo: '))
n2 = int(input('Digite o segundo termo: '))
for c in range(n1, n1 + (10 - 1) * n2 + n2, n2):
    print(c, end=' -> ')
print('Fim')