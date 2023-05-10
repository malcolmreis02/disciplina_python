#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caça ao Tesouro
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
#####################################################

# Leitura da matriz

n = int(input())
matriz = [input().split() for _ in range(n)]

# Leitura e processamento dos caminhos
time_comeca = input()
n_jogadores= int(input())
caminhos = [input() for _ in range(n_jogadores)]


pontuacao = list()
pontuacao2 = [0, 0]

for i in range(n_jogadores):
    pontuacao.append(0)

times=['vermelho', 'azul']

if time_comeca=='azul':
    times = sorted(times)

rodada = 0

def achou(posicao,rodada):
    if posicao=='*':
        pontuacao[rodada]=pontuacao[rodada]+1


for i in caminhos:
    c=0
    r=0
    for j in i:
        if j=='L':
            c+=1
        elif j=='S':
            r+=1
        elif j=='N':
            r-=1
        elif j=='O':
            c-=1
        posicao=matriz[r][c]
        achou(posicao,rodada)
        matriz[r][c]='.'
    rodada+=1

for i in range(len(pontuacao)):
    if i%2==0 or i==0:
        pontuacao2[0]=pontuacao2[0]+pontuacao[i]
    else:
        pontuacao2[1]=pontuacao2[1]+pontuacao[i]

print('Tesouros encontrados pelo time azul: {}'.format(pontuacao2[times.index('azul')]))
print('Tesouros encontrados pelo time vermelho: {}'.format(pontuacao2[times.index('vermelho')]))

if pontuacao2[times.index('azul')]>pontuacao2[times.index('vermelho')]:
    print('Vitoria do time azul')
elif pontuacao2[times.index('azul')]<pontuacao2[times.index('vermelho')]:
    print('Vitoria do time vermelho')
else:
    print('Empate')
        
# Impressão da saída

