#Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
#O programa deverá escrever na tela se o usuário Venceu ou Perdeu

import random
num1 = (random.randint(0,5))
print('='*50)
num2 = int(input('Tente descobrir o número que o computador escolheu.\nO número deve ser entre 0 e 5... '))
print('='*50)
print('O número escolhido foi...', end='')
print(num1)
print('='*30)
if num1 == num2:
    print('Você venceu.Parabéns!')
else:
    print('Você perdeu. Tente novamente!')
print('='*30)
