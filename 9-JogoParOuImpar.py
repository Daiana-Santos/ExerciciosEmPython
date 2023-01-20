#Faça um programa que jogue  Par ou impar com o computador
#O programa só será interrompido quando jogador perder
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
v = 0
while True:
    print('-=' * 16)
    jogador = int(input('Diga um valor: '))
    computador = randint(1, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
        print('-=' * 16)
    print(f'Você jogou {jogador} e o computador {computador}.\nA soma é {total}', end=' ')
    print('...Deu PAR.' if total % 2 == 0 else '...Deu IMPAR.')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você, Venceu!')
            v += 1
        else:
            print('Você, Perdeu!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você, Venceu!')
            v += 1
        else:
            print('Você, Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Game Over!\nVocê venceu {v} vezes. ')
print('-=' * 16)