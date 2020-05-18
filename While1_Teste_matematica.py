#Alunos: João Marcos Oliveira Melo, Ângelo Giordano Silveira, Leandro Moreira Souza

"Faça um programa que use um for como um contador de vidas para resolver perguntas de matematica"
"Caso o usuario perca todas as vidas o jogo acaba!!"

print("\nEsse é um programa para testar sua capacidade de resolver calculos!!!")
print("Você tera 3 vidas para tentar resolver o máximo de perguntas corretamente")
print("Ao final do game lhe direi quantas perguntas você acertou!!!")
print("\nBoa Sorte!!!")

acertos = 0

while True:
    validar = str(input("\nVocê já esta pronto para começar? "))
    if validar == "sim":
        print("Vamos nessa!!!")
        break
    else:
        print("Tudo bem quando estiver pronto!!!")

while True:
    vidas = 3
    calc1=int(input("\nA resposta da expressão (10+10x100) é: "))
    if calc1 == 1010:
        print("Você acertou!!!")
        acertos+=1
    else:
        print("Você errou!!!")
        vidas-=1
    calc2 = int(input("A resposta da expressão (2*2/2+2) é: "))
    if calc2 == 4:
        print("Você acertou!!!")
        acertos+=1
    else:
        print("Você Errou!!!")
        vidas-=1
    calc3 = int(input("A resposta da expressão (4+5x4+1-5+10) é: "))
    if calc3 == 30:
        print("Você acertou!!!")
        acertos+=1
    else:
        print("Você errou!!!")
        vidas-=1
        if vidas <= 0:
            break
    calc4 = int(input("A resposta da expressão (8/2x(2+2) é: "))
    if calc4 == 16:
        print("Você acertou!!!")
        acertos+=1
    else:
        print("Você errou!!!")
        vidas-=1
        if vidas <= 0:
            break
    calc5 = int(input("A resposta da expressão (7+7/7-7+7x7) é: "))
    if calc5 == -48:
        print("Você acertou!!!")
        acertos+=1
    else:
        print("Você errou!!!")
        vidas-=1
        if vidas <= 0:
            break
    break

if vidas >0:
    print("\nVocê conseguiu me vencer parabéns!!!")
    print("Você conseguiu acertar ",acertos," perguntas")
else:
    print("\nVocê perdeu suas vidas tente novamente quando estiver melhor!!!!")
    print("Você conseguiu acertar ", acertos, " perguntas")




