#Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado
#O programa será interrompido quando o número solicitado for negativo.

print('=*'*20)
while True:
    num = int(input('Digite o número para ver tabuada: '))
    if num < 0:
        break
    print('=*' * 20)
    print(f'TABUADA DO {num}')
    print('=*' * 8)
    for cont in range(1, 11):
        resp = num * cont
        print(f'\033[33m{num}\033[m x \033[33m{cont}\033[m = \033[4;31m{resp}\033[m')
    print('=*' * 8)