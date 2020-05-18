#Alunos: João Marcos Oliveira Melo, Ângelo Giordano Silveira, Leandro Moreira Souza

"Faça um programa com For encadeado que mostre a media de cada aluno        "
"de uma determinada turma com a quantidade de alunos que o usúario precisar."

print("Este programa calcula a media de cada aluno da turma!")

numero_alunos = int(input("\nInsira a quantidade de alunos que possui na turma: "))
numero_provas = int(input("Digite a quantidade de provas que cada aluno faz: "))

for x in range(1,numero_alunos+1):
   valor_total_aluno=0
   for y in range(1,numero_provas+1):
       nota = float(input("Digite a nota do %d° aluno na %d° prova: "%(x,y)))
       valor_total_aluno+=nota

   media = valor_total_aluno/numero_provas
   if media>=5:
       print("\nCom a média de %d pontos o %d° aluno está Aprovado!!!"%(media,x))
   else:
       print("\nCom a média de %d pontos o %d° aluno está Reprovado!!!\n"%(media,x))

print("Fim do programa!!!")



