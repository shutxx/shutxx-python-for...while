from random import randint
cpu = randint(0, 10)
print('Acabei de pensar em um número de 0 a 10.')
print('Será q você consegue acertar? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite: '))
    palpite += 1
    if jogador == cpu:
        acertou = True
    else:
        if jogador < cpu:
            print('Mais... Tente novamente.')
        elif jogador > cpu:
            print('Menos... tente novamente.')
print('Acertou com {} tentativas'.format(palpite))
