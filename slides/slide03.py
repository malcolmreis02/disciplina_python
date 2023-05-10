

a, b = 20, 21
#print(a, b)
a >= b
a == b
a != b
a <= b



(a > 0) and (b == 21)
(a > 0) and (b == 20)
(a > 0) or (b == 21)
(a > 0) and not (b == 20)


#O programa a seguir determina se o número digitado é impar ou par

a = int(input('Digite um número: '))
if (a%2)==0:
    print('Esse número é par.')
else:
    print('Esse número é impar.')



#O programa a seguir determina o maior entre dois números
a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
if a==b:
    print('Os dois números digitados são iguais')
elif a>b:
        print('O primeiro número',a, 'é maior que o segundo', b )
else:
    print('O segundo número', b, 'é maior que o primeiro', a)

#o mesmo codigo usando o elif

a = int(input('Digite o primeiro valor:'))
b = int(input('Digite o segundo valor:'))
if a==b:
    print('Os dois números digitados são iguais')
elif a>b:
    print('O primeiro número',a, 'é maior que o segundo', b )
else:
    print('O segundo número', b, 'é maior que o primeiro', a)



#Escreva um programa que, dados três números inteiros, imprima o menor deles
a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite mais um número: '))

if a<=b and a<=c:
    print('O menor número é o ', a)
elif b<=a and b<=c:
    print('O menor número é o', b)
elif c<=a and c<=b: 
    print('O menor número é o ', c)



#Escreva um programa que, dados três números inteiros, imprima os números em ordem crescente.
a = int(input('Digite um número: '))
b = int(input('Digite mais um número: '))
c = int(input('Digite mais um número: '))

if a<=b and b<=c:
    print(a, b, c)
elif a<=b and b>=c:
    print(a, c, b)
elif b<=a and a<=c:
    print(b, a, c)
elif b<=a and a>=c:
    print(b, c, a)
elif c<=a and a<=b:
    print(c, a, b)
else:
    print(c, b, a)



a, b, c, d = 1, 2, 3, 4
print(min(a, b, c, d))
print(max(a, b, c, d))



#Escreva um programa que, dadas duas datas, determine qual
#delas ocorreu cronologicamente primeiro. Para cada uma das
#duas datas, leia três números referentes ao dia, mês e ano,
#respectivamente.

dia1 = int(input('Digite o primeiro dia: '))
mes1 = int(input('Digite o primeiro mês: '))
ano1 = int(input('Digite o primeiro ano: '))

dia2 = int(input('Digite o segundo dia: '))
mes2 = int(input('Digite o segundo mês: '))
ano2 = int(input('Digite o segundo ano: '))

if ano1>=ano2:
    if mes1>=mes2:
        if dia1>=dia2:
            print('A primeira data é a segunda.')
            print(dia2, mes2, ano2, sep='/')
        else:
            print('A primeira data é a primeira')
            print(dia1, mes1, ano1, sep='/')
    else:
        print('A primeira data é a segunda.')
        print(dia2, mes2, ano2, sep='/')
else:
    print('A primeira data é a primeira.')
    print(dia2, mes2, ano2, sep='/')




#Escreva um programa que calcule as raízes de uma equação de
#segundo grau. O seu programa deve receber três números a, b e
#c, sendo que a equação é definida como ax2 + bx + c = 0. O seu
#programa também deve tratar o caso em que a = 0

a = int(input('Sabendo da estrutura da equação do segundo grau (ax2 + bx + c = 0), com a, b, c inteiros, digite o a da sua equação: '))
b = int(input('digite o b da sua equação: '))
c = int(input('digite o c da sua equação: '))

delt = (b**2) - (4*a*c)
xpo = (-b + (delt)**(1/2))/2*a
xne = (-b - (delt)**(1/2))/2*a



if a==0:
    if b==0:
        print('Essa equação não possui raiz')
    else:
        xaz = -c/b
        print('A raiz da sua equação é', xaz)
else:
    if xpo == xne:
        print('A raiz da sua equação é', xpo)
    else:
        print('As duas raizes da sua equação são', xpo, 'e', xne)


#Escreva um programa que simula o jogo conhecido como
#“Pedra, Papel e Tesoura” de um jogador A contra um jogador B.
#O programa deve ler a escolha do jogador A e a escolha do
#jogador B. Por fim, o programa deve indicar quem foi o vencedor.

print('Vamos jogar pedra, papel e tesoura!!!')
ja = input('Jogador A, digite sua escolha: ')
jb = input('Jogador B, digite sua escolha: ')


if ja!=('pedra' or 'papel' or 'tesoura') or jb!=('pedra' or 'papel' or 'tesoura'):
    print('Opções inválidas!', 'Escolham entre "pedra", "papel" ou "tesoura"', end='\n')
elif ja==jb:
    print('Empate!!')
else:
    if ja=='papel':
        if jb=='tesoura':
            print('O jogador B ganhou!!')
        else:
            print('O jogador A ganhou!!')
    elif ja=='pedra':
        if jb=='papel':
            print('O jogador B ganhou!!')
        else:
            print('O jogador A ganhou!!')
    elif ja=='tesoura':
        if jb=='pedra':
            print('O jogador B ganhou!!')
        else:
            print('O jogador A ganhou!!')
