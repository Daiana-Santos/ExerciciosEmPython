#Faça um programa que mostre na tela a contagem regressiva para o estouro de fogos de artificios
#início de 10 até 0 com uma pausa de 1segundo entre eles

from time import sleep
import emoji
for contador in range(10, -1, -1):
    print(contador)
    sleep(0.5)
print(emoji.emojize('HAPPY NEW YEAR!:fireworks:'))
