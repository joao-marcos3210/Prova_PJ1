#Alunos: João Marcos Oliveira Melo, Ângelo Giordano Silveira, Leandro Moreira Souza

"Faça um programa utilizando IF e que faça perguntas a cerca de uma cena de crime"
"E que defina a posição do usuário diante do crime!!!"

ct_crime = 0
print("\nPrazer meu nome é Jack, e eu sou o detetive dessa cidade!!!")
print("Vamos dar uma olhada na sua situação")
print("Você foi encontrado ao lado do corpo de Melanine Beatrice")
print("Você diz que é inocente mas mesmo asssim preciso te fazer algumas perguntas!")
print("Responda as perguntas com {sim} ou {não}")
print("Ao final lhe direi sua situação!!!")

while True:
    validar = str(input("\nVocê está pronto para começar? "))
    if validar == "sim":
        print("Então vamos começar:")
        break
    else:
        validar2 = str(input("\nVocê quer revisar a história? "))
        if validar2=="sim":
            print("\nPrazer meu nome é Jack, e eu sou o detetive dessa cidade!!!")
            print("Vamos dar uma olhada na sua situação")
            print("Você foi encontrado ao lado do corpo de Melanine Beatrice")
            print("Você diz que é inocente mas mesmo asssim preciso te fazer algumas perguntas!")
            print("Responda as perguntas com {sim} ou {não}")
            print("Ao final lhe direi sua situação!!!")
        else:
            print("\nTudo bem quando você estiver pronto nós começamos!!!")


quest1=str(input("\nTelefonou para a vítima? "))
if quest1=="sim":
    ct_crime+=1
quest2=str(input("Esteve no local do crime? "))
if quest2=="sim":
    ct_crime+=1
quest3=str(input("Mora perto da vítima? "))
if quest3=="sim":
    ct_crime+=1
quest4=str(input("Devia para a vítima? "))
if quest4=="sim":
    ct_crime+=1
quest5=str(input("Já trabalhou com a vítima? "))
if quest5=="sim":
    ct_crime+=1

if ct_crime<2:
    print("\nVocê é considerado inocente!!!")
elif ct_crime==2:
    print("\nVocê é considerado suspeito!!!")
elif ct_crime>=3 and ct_crime<=4:
    print("\nVocê é considerado Cúmplice!!!")
else:
    print("\nVocê é o Assassino!!!")

print("\nFim do programa!!!")