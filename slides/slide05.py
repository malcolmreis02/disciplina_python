
letras = ["A", "B", "C", "D", "E", "F", "G", "H"]
print(len(letras))
print(letras[0])
print(letras[1:4])
print(letras[-1]) #de tras pra frente
print(letras[-4:]) #4 ultimos numeros da lista
type(letras)
'I' in letras
'A' and 'B' in letras
letras.append('Malcolm')
print(letras)
letras.insert(1, 'segunda posição')
letras.insert(300, 'teste') #de qualquer forma, se a posição for maior que o tamanho da lista, o novo objeto vai para o final da lista
print(letras.index('C'))
letras.remove('C')
print(letras)
letras.pop() #removendo o último objeto
letras.pop(1) #removendo o segundo objeto da lista
letras.count('C') #verificando quantas vezes a letra 'A' aparece na lista
letras.reverse() #inverte a ordem dos objetos na lista
letras.sort(reverse = True) # ordena a lista de forma decrescente, crescente é False
print(sorted(letras)) #printa a lista de forma ordenada de forma crescente
letras2 = letras.copy()





# Escreva um programa que recebe como entrada um número
# inteiro positivo n. Em seguida, seu programa deve ler n
# números inteiros e adicioná-los em uma lista. Por fim, seu
# programa receberá um número inteiro x e deve verificar se x
# pertence ou não à lista

n = int(input('Digite a quantidade de números que serão inseridos: '))
lista = list()
i = 1

while i <= n:
    lista.append(int(input('Digite o seu número: ')))
    i= i+1
print(lista)

x_procurado = int(input('Qual número eu devo procurar? \n'))
if x_procurado in lista:
    print('Esse número está na lista.')
else:
    print('Esse número não está na lista.')



# Escreva um programa que leia números positivos e os armazene
# numa lista (até que um número não positivo seja fornecido).
# Por fim, seu programa receberá um número inteiro x e deve
# verificar se x pertence ou não à lista.

lista = list()
lista.append(int(input('Digite o primeiro número: ')))
while True:
    x = int(input('Digite outro número: '))
    if x>=0:
        lista.append(x)
    else:
        break
x_procurado = int(input('Digite o número que devo procurar: '))
if x_procurado in lista:
    print('Esse número está na lista.')
else:
    print('Esse número não está na lista.')



n = int(input('Quantos números serão lidos: '))
lista = [int(input('Digite um número para a lista: ')) for i in range(n)]
print(lista)
x_remover = int(input('Qual número deve ser removido da lista: '))
lista = [i for i in lista if x_remover!=i]
print(lista)



###### EXERCÍCIO
vingadores = ['Homem de Ferro', 'Capitão América', 'Thor', 'Hulk', 'Viúva Negra', 'Gavião Arqueiro']
print('Esses são os vingadores:\n', vingadores, sep='')
# Agora, inclua o Homem-Aranha no final da lista e imprima em qual posição está o Thor.
vingadores.append('Homem Aranha')
print('O Thor está na posição', vingadores.index('Thor'))
#Infelizmente a Viúva Negra e o Homem de Ferro não fazem mais parte da Iniciativa Vingadores, então retire-os da lista
if 'Viúva Negra' in vingadores:
    vingadores.remove('Viúva Negra')
    print('Viúva Negra foi desligada dos vingadores')
if 'Homem de Ferro' in vingadores:
    vingadores.remove('Homem de Ferro')
    print('Homem de Ferro foi desligado dos vingadores')
print('Esses são os atuais vingadores:\n', vingadores, sep='')



tupla = (1, 2, 3)
tupla[1]
tupla2 = (1,)
type(tupla2)



# Dada uma lista L de n valores inteiros, escreva um programa que remova todos os números pares da lista.
n = int(input('Quantos números serão lidos: '))
lista = [int(input('Digite um número: ')) for i in range(n)]
for i in lista:
    if i%2==0:
        lista.remove(i)
print(lista)



# Dadas duas listas P1 e P2, ambas com n valores reais que
# representam as notas de uma turma na prova 1 e na prova 2,
# respectivamente, escreva um programa que calcule a média da
# turma nas provas 1 e 2, imprimindo em qual das provas a turma
# obteve a melhor média.

n = int(input('Quantos alunos têm na turma?\n'))
P1 = [int(input('Digite a nota da primeira prova do aluno: ')) for i in range(n)]
P2 = [int(input('Digite a nota da segunda prova do aluno: ')) for i in range(n)]
if sum(P1)/len(P1)>sum(P2)/len(P2):
    print('Os alunos foram melhores na primeira prova.')
elif sum(P1)/len(P1)==sum(P2)/len(P2):
    print('Os alunos obtiveram rendimentos semelhantes nas duas provas.')
else:
    print('Os alunos foram melhores na segunda prova.')



# Dadas duas listas L1 e L2, com n e m valores inteiros,
# respectivamente, escreva um programa que concatene as listas L1
# e L2 em uma nova lista L3. Em seguida, imprima a lista L3 ordenada
# de maneira crescente e decrescente.

n = int(input('Quantos números terá na Lista 1?\n'))
m = int(input('Quantos números terá na Lista 2?\n'))
L1 = [int(input('Digite um número para a Lista 1: ')) for i in range(n)]
L2 = [int(input('Digite um número para a Lista 2: ')) for j in range(m)]

L3 = L1 + L2
L3_cres = sorted(L3)
L3.reverse
print('Lista 3 em ordem crescente:', L3_cres, 'Lista 3 em ordem decrescente:', L3, sep='\n')
