from random import randint
from time import sleep
n = randint(0, 5)
n_1 = int(input('Vou pensar num número de 0 a 5, tente adivinhar: '))
print('PROCESSANDO...')
sleep(2)
if n_1 == n:
    print('Parabéns, você acertou o número!')
else:
    print(f'Você errou o número, eu pensei no {n}, tente novamente.')
print('Reinicie para jogar de novo.')