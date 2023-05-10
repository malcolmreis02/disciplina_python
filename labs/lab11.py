#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Encaixe 2D
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
#####################################################

# Leitura do tabuleiro
T = int(input())
tabuleiro = []
for _ in range(T):
  tabuleiro.append(input().split())

# Leitura da peça
P = int(input())
peca = []
for _ in range(P):
  peca.append(input().split())

# Função que rotaciona uma matriz em 90° (sentido horário) n_rot vezes
def rot(m, n_rot):
    if n_rot == 0:
        return m
    if n_rot > 1:
        m = rot(m, n_rot-1)
    return [[m[j][i] for j in range(len(m)-1,-1,-1)] for i in range(len(m[0]))]


t_x, t_y = len(tabuleiro), len(tabuleiro[0]) # Dimensões do tabuleiro
lista_N_encaixes = [] # Lista para armazenar o numero de encaixes em cada orientação da peça

n_preenchidos_peca = 0 # Encontrando o numero de células preenchidas na peça
p_x, p_y = len(peca), len(peca[0])
for p_i in range(p_x):
    for p_j in range(p_y):
        if peca[p_i][p_j] == "X":
            n_preenchidos_peca += 1

for n_rot in range(0,4): # Encontrando o número de encaixes para cada orientação da peça
    peca_rot = rot(peca, n_rot) # Rotaciona a peça n_rot vezes
    p_x, p_y = len(peca_rot), len(peca_rot[0]) # Dimensões da peça rotacionada
    N_encaixes = 0 # Número de encaixes nesta orientação específica
    for t_i in range(t_x-p_x+1): # Checando o encaixe em cada posição possível
        for t_j in range(t_y-p_y+1):
            n = 0
            for p_i in range(p_x):
                for p_j in range(p_y):
                    if peca_rot[p_i][p_j]=="." or tabuleiro[t_i+p_i][t_j+p_j] == peca_rot[p_i][p_j]:
                        pass
                    else:
                        n+=1
            if n==n_preenchidos_peca: # Se o número de células compatíveis for igual ao número de células preenchidas temos um encaixe
                N_encaixes+=1
    lista_N_encaixes.append(N_encaixes) # Armazena o número de encaixes desta rotação

# Exibe os resultados
n0,n90,n180,n270 = lista_N_encaixes
print("{},{},{},{}".format(n0,n90,n180,n270))