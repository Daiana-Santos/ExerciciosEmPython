# Melhore o jogo do desafio 28 onde o computador vai pensar em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessarios para vencer.

from random import randint
computador = randint(0,10)
print('==*'*15)
print('Sou o seu Computador...\n Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi? ')
print('==*'*15)
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('É um número maior... Tente outra vez.')
        elif jogador > computador:
            print('É um número menor... Tente outra vez.')
    print('==*' * 15)
print('Acertou com {} tentaivas. Parabéns!'.format(palpite))