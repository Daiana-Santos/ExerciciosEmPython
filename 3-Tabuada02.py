#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
#Usando o laço For

print('~'*20)
num = int(input('Digite um número: '))
print('A tabuada do numero {} é:'.format(num))
print('~'*20)
for cont in range(1,11):
    resp = num * cont
    print(f'\033[33m{num}\033[m x \033[33m{cont}\033[m = \033[4;31m{resp}\033[m')
print('~'*20)

