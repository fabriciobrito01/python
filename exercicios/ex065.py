c = n = m = maior = menor = q = 0
esc = 'S'
while esc == 'S':
    n = int(input('Digite um número: '))
    c += n
    m = c / n
    q += 1
    if q == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    esc = str(input('Deseja continuar? [S/N]')).upper()
print(f'A quatidade de números digitas foi {q}.')
print(f'A soma dos números foi igual a {c}.')
print(f'A média dos números foi igual a {m}.')
print(f'O menor número foi {menor} e o maior foi {maior}.')
