print('=+' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('=+' * 20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n1 = n
c = 1
while c <= 10:
    n1 += r
    c += 1 
    print(n1, end=' -> ')
print('FIM')