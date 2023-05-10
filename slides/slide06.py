
print('você respondeu \'sim\'') # para uma string que contem algo entre aspas
print('Malcolm\'s Home') #para adicionar apenas um apostrofe
print('um\ndia\nserei\nrico') # para adicionar uma quebra de linha
print('\t Comecemos este conto') # para adicionar um paragrafo com aquele espaço inicial

msg = 'hello world'
print(len(msg))
print(msg[0]) #acessando elementos de uma string
print(msg[1:]) #toda a mensagem do index 1 adiante
print(msg[1:4]) #a mensagem do index 1 ao 3
print(msg[1::2]) # mensagem vai do primeiro ao final de dois em dois
print(msg.startswith('hello')) #verificando se msg começa com hello


print(format(10, 'd')) #numero inteiro
print(format(10, 'f')) #numero real
print(format(10, '+f')) #com sinal sendo positivo ou negativo
print(format(3.14159265359, '+.10f')) #formatando com sinal e com arredondamento preciso

frutas = 'Temos as frutas: {0}, {1}, {2} e {3}.'
print(frutas.format('abacaxi', 'maça', 'pêra', 'uva'))

nota = 'sua nota foi igual a {0:.3f}' #aqui ele coloca 3 numeros depois da virgula arredondando o ultimo digito
print(nota.format(8.7777))

dia_tempo = 'hoje é dia {0:02d}/{1:02d}/{2} e a temperatura é de {3:.1f}C' #em 02d, ele printa obrigatoriamente dois digitos como 01, 02 e nao apenas 1 ou 2
print(dia_tempo.format(5,4,2022,25.1354))

frase = 'um dia sonhei com isso'
prova = 'eu, malcolm, vou te provar'
frase.split('')

s1, s2 = input().split()
print(s1, s2, sep='\n')

a, b, c = [int(i) for i in input('insira separando com espaços os coeficientes da equação sendo ax² + bx + c = 0:\n').split()]

numeros = [int(i) for i in input('vai inserindo qualquer número separando-os por um espaço: \n').split()] 

frutas = [str(i) for i in input('vai colocando nome de frutas separadamente: \n').split()]
frutas_txt = ', '.join(list(frutas)) #tem que estar em lista pra dar certo
print(frutas_txt)   

nome = 'malcolm Dos Reis'
print(list(nome))
print(nome.capitalize())
print(nome.lower())
print(nome.upper())

a = 'a, b, c, d'
b = a.replace(', ', ' ')
print(b)

teste = '1234'
print(teste.isnumeric()) #vendo se a string tem apenas numeros
print(teste.isalpha()) #vendo se a string contem apenas letras
'''


########## EXERCICIOS

'''
# Escreva um programa que, dada uma sequência de números inteiros
# (todos fornecidos na mesma linha, separados por espaços), imprima
# a média desses números

numeros = [int(i) for i in input('Digite os números separados por um espaço: \n').split()]
media = sum(numeros)/len(numeros)
print(media)
'''

'''
# Escreva um programa que, dada uma String representando um
# texto, imprima o número de palavras existentes. Observação: você
# deve remover os sinais de pontuação (“.”, “,”, “:”, “;”, “!” e “?”)
# antes de realizar a contagem das palavras.

frase = input('Digite qualquer frase:\n').split()
frase2 = list()
for i in frase:
    if '.' in i:
        i = i.replace('.', '')
        frase2.append(i)
    elif ',' in i:
        i = i.replace(',', '')
        frase2.append(i)
    elif ':' in i:
        i = i.replace(':', '')
        frase2.append(i)
    elif ';' in i:
        i = i.replace(';', '')
        frase2.append(i)
    elif '!' in i:
        i = i.replace('!', '')
        frase2.append(i)
    elif '?' in i:
        i = i.replace('?', '')
        frase2.append(i)
    else:
        frase2.append(i)
print('Essa frase tem {} palavras.'.format(len(frase2)))
print(frase2)
'''

'''
# Um palíndromo é uma palavra ou frase que pode ser lida da mesma
# forma tanto da esquerda para a direita como da direita para a
# esquerda (desconsiderando os espaços em branco). Considere que a
# entrada não possui sinais de pontuação ou acentos. Escreva um
# programa que, dada uma String, verifique se ela é um palíndromo.

a = str(input('Digite uma palavra:\n'))
a2 = list()

print(a[0])

for i in a:
    a2.insert(0,i)
a_txt = ''.join(a2)

if a==a_txt:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
