from random import randint
num_pc = randint(1, 10)
num_user = 0
tentativas = 0
while num_user != num_pc:
    num_user = int(input('Adivinhe o número que o computador está pensando: '))
    tentativas += 1
    if num_user > num_pc:
        print('Um pouco menos...')
    elif num_user < num_pc:
        print('Um pouco mais...')
print(f'Parabéns, você acertou em {tentativas} tentativas.')