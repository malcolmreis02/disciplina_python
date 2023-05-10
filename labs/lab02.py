###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Rumo a Marte
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
# Link do enunciado: https://susy.ic.unicamp.br:9999/mc102/02/enunciado.html
###################################################

# Leitura de dados

D1 = int(input())
V1 = int(input())
T = int(input())
D2 = int(input())
V2 = int(input())

# Cálculo do tempo total gasto por cada espaçonave 
T1 = (D1/V1)
T2 = (D2/V2)
TT = T*24

# Impressão da resposta

print(T1 < (T2 + TT))