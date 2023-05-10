def bubbleSort(lista):
    n = len(lista)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                (lista[j], lista[j+1]) = (lista[j+1], lista[j])
    return lista

teste1 = [1, 2, 3, 6, 7, 8, 2, 5, 7]
#print(bubbleSort(teste1))

## ordenando os itens de uma lista realizando trocas (vendo o primeiro e o segundo elemento e se o primeiro for maior que o segundo,
# trocamos, e assim por diante, o segundo com terceiro, ate chegar no penultimo com o ultimo)

def indiceMenor(lista, inicio):
    minimo = inicio
    n = len(lista)
    for j in range(inicio +1, n):
        if lista[minimo]>lista[j]:
            minimo = j
    return minimo
def selectionSort(lista):
    n = len(lista)
    for i in range(n-1):
        minimo = indiceMenor(lista, i)
        (lista[i], lista[minimo]) = (lista[minimo], lista[i])
    return(lista)

#print(selectionSort(teste1))
## ordenando os elementos de uma lista localizando os numeros menores e colocando em primeiro:
# busca o menor de todos os elementos e coloca em primeiro, busca o menor de todos os elementos
# a partir do primeiro e o coloca em segundo, e assim por diante

def insertion(lista, i):
    j = i - 1
    while (j >= 0) and (lista[j] > lista[i]):
        j = j - 1
        lista[j + 1:i + 1] = [lista[i]] + lista[j + 1:i]
def insertionSort(lista):
    n = len(lista)
    for i in range(1, n):
        insertion(lista, i)
    return lista

print(insertionSort(teste1))
