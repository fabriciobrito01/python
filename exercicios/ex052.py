n = int(input('Digite um número inteiro: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\33[34', end='')
    else:
        print('\33[31', end='')
    print(f'{c}, end=')