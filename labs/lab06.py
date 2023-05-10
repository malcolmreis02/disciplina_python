##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Torre de Panquecas
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642+.
##################################################

# Leitura da torre de panquecas
torre = [int(panqueca) for panqueca in input().split()]
movimentos = list()

while True:
    ent = int(input())
    movimentos.append(ent)
    if ent == 0:
        break

movimentos.pop()

# Leitura e processamento dos movimentos

for i in movimentos:
    n_torre = torre[:i]
    n_torre.reverse()
    torre = n_torre + torre[i::]

# Impressão da saída

torre2 = torre.copy()

torre2.sort(reverse=False)

if torre2==torre:
    print('Torre estavel')
else:
    print('Torre instavel')