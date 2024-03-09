print('=+' * 20)
print('PROGRESSÃO ARITMÉTICA')
print('=+' * 20)
n = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
n1 = n
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(n1, end=' -> ')
        n1 += r
        c += 1 
    print('PAUSA')
    mais = int(input('Quantos termos mais deseja ver? '))
print(f'Progressão finalizada com {total} termos mostrados.')