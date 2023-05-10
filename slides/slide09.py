l = int(input('digite o n de linhas: '))
c = int(input('digite o n de colunas: '))
matriz = [[0 for j in range(c)] for i in range(l)]
matriz[0][1] = 3 #alterando o valor de uma matriz sendo matriz[l][c]
print(matriz)

A = [[1, 2], [3, 4]]
B = [linha.copy() for linha in A] #copiando uma matriz sem afetar a original

