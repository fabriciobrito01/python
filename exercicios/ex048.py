from time import sleep
s = 0
count = 0
for c in range(0, 500):
    if c % 2 != 0 and c % 3 == 0:
        s += c  # mesma coisa que s = s + c
        count += 1
        print(c)
        sleep(0.1)
print(f'A soma dos {count} valores é igual a {s}.')