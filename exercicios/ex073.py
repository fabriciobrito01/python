brasileirao = ('Botafogo', 'Palmeiras', 'Fluminense', 'Cruzeiro', 'Atheletico-PR', 
               'Atlético-MG', 'Santos', 'Fortaleza', 'Flamengo', 'São Paulo', 'Grêmio', 'Internacional', 'Bragantino', 'Bahia', 
               'Goiás', 'Vasco', 'Corinthians', 'Cuiabá', 'Coritiba', 'América-MG')

print(f'Tabela Brasileirão 2023: {brasileirao}')
print(f'G5: {brasileirao[0:5]}')
print(f'Z4: {brasileirao[-5: -1]}')
print(f'Ordem alfabética: {sorted(brasileirao)}')
print(f'O Flamengo está na {brasileirao.index("Flamengo")-1}ª posição')