#Alunos: João Marcos Oliveira Melo, Ângelo Giordano Silveira, Leandro Moreira Souza

"Faça um program que por meio de uma função que calcule a formula de Bhaskara,"
"e que na função main o usúario somente precise passar os valores das variáveis."

print("\nPrograma que calcula a equação de Bhaskara!!!\n")

def verificadelta(num,a,b):
    if num>0:
        x1=(-b+(num**(1/2)))/(2*a)
        x2=(-b-(num**(1/2)))/(2*a)
        print("\nO valor de x1 é: %.2f"%(x1))
        print("O valor de x2 é: %.2f"%(x2))
    elif num==0:
        x1=(-b+(num**(1/2)))/(2*a)
        print("\nO valor de x1 é: %2.f"%(x1))
    elif num<0:
        print("\nA equação não possui raíz real!!")

def bhaskara(a,b,c):
    delta = (b*b)-(4*a*c)
    verificadelta(delta,a,b)

if __name__ == '__main__':
    numero1=int(input("Insira o valor da variável {a}: "))
    numero2=int(input("Insira o valor da variável {b}: "))
    numero3=int(input("Insira o valor da variável {c}: "))
    bhaskara(numero1,numero2,numero3)
    print("\nFim do Programa!!!")

