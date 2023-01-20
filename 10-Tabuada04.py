def cabeçalho():
    print('=*' * 20)
    print(f'TABUADA DO {num}')
    print('=*' * 8)


def tabuada():
    for cont in range(1, 11):
        resp = num * cont
        print(num, 'x', cont, '=', resp)
    print('=*' * 8)


# Programa Principal
repetir = ' '
while repetir not in 'Nn':
    print('=*' * 20)
    num = int(input('Digite o número para ver tabuada: '))
    print(cabeçalho())
    print(tabuada())
    repetir = str(input('Quer ver outra tabuada?[S/N] '))
print('=*' * 20)


