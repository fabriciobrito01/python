n = c = s = 0
while True:
    n = int(input( 'Digite um número [999 p/ parar]: '))
    c += 1
    if n == 999:
        break
    s += n
print(f'A soma entre os {c} números foi {s}.')

n = c = s = 0
while n != 999:
    s += n
    c += 1
    n= (int(input('Digite um número [999 p/ parar]:  ')))
print(f'A soma entre os {c} números foi {s}. ')