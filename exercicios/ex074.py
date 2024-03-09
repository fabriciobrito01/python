from random import randint
maior = menor = 0
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'''
Os números sorteados foram: {n}.
O maior número foi {max(n)}.
O menor número foi {min(n)}.''')