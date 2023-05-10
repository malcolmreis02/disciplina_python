print('Hello, world!!')
print('dia 1', 'dia 2', 'dia 3', 'dia 4') #automaticamente separados por um espaço
print('separados', 'por', 'mais', sep='+') #separados por um sinal de mais

print('sem quebra de ', end='') #para tirar a quebra de linha depois de dar um print
print('linha')

print('quero', 'algo', 'diferente', sep='--', end='!\n') #barra ao contrario e n joga uma quebra de linha

print ('malcolm - 187642 - MC102 - 2022')
print('malcolm', '187642', 'MC102', '2002', sep = ' - ')

a = 1
b = 1.2
c = 'um dia'
d = True
type(c)

pi = 3.1416
a = b = 2 #atribuindo valores iguais a variaveis diferentes
a, b = 1, 3 #atribuindo valores diferentes para variaveis diferentes
print(a, b)

5/2 #divisao normal
5//2 #divisão inteira
2**3 #exponencial
5%2 #resto da divisão inteira

a = 1
b = 2
a += b #isso é igual a a = a+b, o mesmo para os outros operadores
a

nome_unicamp = 'Universidade ' + 'Estadual ' + 'de ' + 'Campinas'
print(nome_unicamp)

nome = 'Malcolm'
local = ', você está na unicamp'
print(nome + local)

print(3* 'Malcolm ')
print('a', 'b'*2, sep='')
print(('a' + 'b') *3)

2>3
3>1
3==1
3==3
2+3==5

(2==3) and (2>1)
(2==3) or (2>1)

not True
not (True and False)

a = 1
type(a)
a = float(a)
type(a)

c = 2
type(c)
c = str(c)
cc = bool(c)
type(cc)

a = True
a = int(a)
a

a = 6
b = 8
hip = (a**2 + b**2)**(1/2)
hip

a_str = int(input('digite o tamanho do primeiro cateto: '))
b_str = int(input('digite o tamanho do segundo cateto: '))
hip = (a**2 + b**2)**(1/2)
print(hip)
