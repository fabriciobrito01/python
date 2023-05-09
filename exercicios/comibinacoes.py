from itertools import combinations

numeros = list(range(1, 26)) # Cria uma lista de números de 1 a 25

with open("combinacoes2.txt", "w") as f:
    for comb in combinations(numeros, 15):
        print('.')
        f.write(''.join(str(num) for num in comb) + '\n')
        print(comb)
count = comb.count('.')
print(count)