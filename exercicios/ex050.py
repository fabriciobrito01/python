s = 0
count = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º número inteiro: '))
    if n % 2 == 0:
        s += n
        count += 1
print(f'A soma dos {count} números pares digitados é igual a {s}.')