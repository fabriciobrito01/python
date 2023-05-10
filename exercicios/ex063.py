n = int(input('Quantos termos deseja ver? '))
t1 = 0
t2 = 1
c = 3
print(f'{t1} -> {t2}', end='')
while c <= n:
    c += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(f' -> {t3}', end='')
print('FIM.')