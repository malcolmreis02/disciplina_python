
i = 1
while i<=10:
    print(i)
    i = i+1



#Dados dois números inteiros positivos, calcule o quociente e o
#resto da divisão inteira entre os dois, usando apenas somas e
#subtrações.

a = int(input('Digite o dividendo: '))
b = int(input('Digite o divisor: '))
quo = 0

while b<=a:
    a = a-b
    quo = quo + 1
print('O resto da divisão é', a)
print('o quociente da divisão é', quo)



#Dado um número inteiro positivo n, calcular o valor de n!
a = int(input('Digite um número inteiro: '))
i = 1
fat = 1

while i<a:
    fat = fat*i
    i= i +1
print(fat)



lista_teste = [1, 'meu', 12, True, 5.6]
lista_teste[0]
lista_teste[0]*lista_teste[2]
len(lista_teste)



lista_teste = [1, 'meu', 12, True, 5.6]
i=0

while i<len(lista_teste):
    print(lista_teste[i])
    i=i+1



numeros = [1, 10, 3, 4, 5, 6, 7]
max(numeros)
min(numeros)
len(numeros)



#for para percorrer uma lista
numeros = [1, 10, 3, 18, 5, 6, 7]
i = 0
maximo = 0

for i in numeros:
    if i>maximo:
        maximo = i
print(maximo)



a = list(range(0, 12))
b = list(range(0, 100, 10))
c = list(range(0, -5,-1))


for i in list(range(10)):
    print('julia')



n = int(input('Digite um número: '))
for i in range(1, n+1):
    print(i)



n = int(input("Digite um número inteiro positivo: "))
potencia = 1
for i in range(n):
    potencia = potencia * 2
    print(potencia)
#aqui ele apenas está repetindo o processo n vezes, nao necessariamente usando algum elemento do range(3)



#calculando n!
n = int(input("Digite um número inteiro positivo: "))
fat=1
for i in range(1, n+1):
    fat = fat*i
    i = i+1
print(fat)



# Determinando a quantidade de números inteiros positivos
# fornecidos para um programa (até a leitura de um inteiro não
# positivo).

n=0
while True:
    x = int(input('Digite um número inteiro: '))
    if x<=0:
        break
    n=n+1
print('Você digitou', n, 'números antes de inserir um número negativo!')



# Encontrando um elemento x em uma lista.
x = int(input('Digite um número inteiro: '))
list1 = [1, 12, 3, 4, 5, 6, 7, 8, 9]

for i in list1:
    if x==i:
        print('Seu número está na lista!')
        break
else:
    print('Seu número não está na lista!!')



list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    if i%2==1:
        continue
    print(i)



n = int(input("Entre com o número de linhas: "))
m = int(input("Entre com o número de colunas: "))

for i in range(n):
    for j in range(m):
        print('#', end='')
    print()



#Imprimindo todos os horários de um dia, no formato HH:MM (horas e minutos).

for i in range(24):
    for j in range(60):
        print(i, ':',j, sep='', end='\n')



for h in range(24):
    for m in range(60):
        print('{:02d}:{:02d}'.format(h, m))


######  EXERCICIOS ######


#Escreva um programa que leia um número inteiro positivo
#(n > 1) e imprima os seus divisores.

n = int(input('Digite um número inteiro positivo: '))
for i in range(1, n+1):
    if n%i==0:
        print(i, 'é um divisor de', n)


#Escreva um programa que leia um número inteiro positivo
#(n > 1) e imprima o número de seus divisores.
n = int(input('Digite um número inteiro positivo: '))
count = 0
for i in range(1, n+1):
    if n%i==0:
        count= count+1
print('Esse número tem', count, 'divisores')


#Escreva um programa que leia um número inteiro positivo
#(n > 1) e determine se ele é primo.
n = int(input('Digite um número inteiro positivo: '))
count = 0
for i in range(1, n+1):
    if n%i==0:
        count= count+1
if count==2:
    print('É um número primo')


# Escreva um programa que leia um número inteiro positivo (n > 1) e imprima sua fatoração em números primos.
n = int(input('Digite um número inteiro positivo: '))
i = 2
while n!=1:
    while n%i == 0:
        print(i)
        n = n/i
    i = i+1














































