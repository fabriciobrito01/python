from math import factorial
n = int(input('Digite um número para calcular o seu Fatorial: '))
c = n
print(f'{n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    c -= 1
    print(' X ' if c >= 1 else ' = ', end ='')
print(factorial(n), end='')