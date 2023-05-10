def primeira_funcao():
    print('essa é a minha primeira funcao')
#primeira_funcao()

mensagem = 'bom dia'
def mandar_mensagem(msg):
    print(msg)
#mandar_mensagem(mensagem)

def soma(x, y):
    print(x+y)
#soma(1, 2)

def duplica_ultimo(lista):
    lista.append(lista[-1])
numeros = [1, 2, 3]
#duplica_ultimo(numeros.copy()) #sem alterar a lista original

def mensagem2():
    return 'bom dia'
x = mensagem2()
#print(x)

#### EXERCICIOS

#Escreva uma função que, dados dois números inteiros positivos,
#calcule e retorne o Máximo Divisor Comum (MDC) entre os dois.

def funcao1(a, b):
    lista_a = list()
    lista_b = list()
    for i in range(a):
        i+=1
        if a%i==0:
            lista_a.append(i)
    for j in range(b):
        j+=1
        if b%j==0:
            lista_b.append(j)
    lista = [value for value in lista_a if value in lista_b]
    MDC = max(lista)
    print(MDC)

funcao1(15,10)




































