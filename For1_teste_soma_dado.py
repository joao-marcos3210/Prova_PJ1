#Alunos: João Marcos Oliveira Melo, Ângelo Giordano Silveira, Leandro Moreira Souza

"Faça um programa que use um For para mostrar 6 combinações de dados aleatórias."
"Faça p usuário ter um tempo para somar todas as 6 combinações e ao final dizer a soma certa."

import time
import random
num = 0
ct_acerto = 0


print("\nEsse é um jogo onde irá aparecer 6 lados de um dado!!!")
print("Seu desafio é somar os 6 lados do dado o mais rápido possível!!!")
print("Caso queira sair é so digitar {0}!!!")
print("Boa sorte!!!")


def tempo():
    ct_tempo=0
    for x in range(10):
        time.sleep(1)
        ct_tempo+=1
    return ct_tempo

while True:
    validar=str(input("\nVocê ja está pronto para começar? "))
    if validar=="sim":
        time.sleep(1)
        print("\nVamos lá!!!")
        break
    else:
        print("Certo quando estiver pronto!!!")

while True:
    soma = 0
    for x in range(6):
        num = random.randrange(1,6)
        print(num)
        soma+=num
    quest=int(input("\nA soma dos 6 valores é de: "))
    if quest == 0:
        print("\nVocê saiu!!!")
        print("Você acertou ",ct_acerto," vezes!!!!")
        break
    else:
        if quest == soma:
           print("\nParabéns você venceu no desafio!!!")
           ct_acerto+=1
        else:
           print("\nVocê perdeu no meu desafio!!!")
           print("Tente novamente!!!")

