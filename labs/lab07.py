###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Disconnect
# Nome: Malcolm dos reis Alves Pereira
# RA: 187642
###################################################

# Leitura das tropas de defesa

qnt_defesa = int(input())
defesa = list()
for i in range(qnt_defesa):
    defesa.append(int(input()))
defesa2 = defesa.copy()

# Leitura das tropas de ataque

qnt_ataque = int(input())
ataque = list()
for i in range(qnt_ataque):
    ataque.append(int(input()))

# Processamento da guerra

rodadas = len(defesa)-len(ataque)+1
confirmacao_venceu = 0

for n in range(rodadas):
    cont_vitorias = 0
    cont_derrotas = 0

    for i in range(len(ataque)):
        if ataque[i]-defesa[i+n]>0:
            cont_vitorias+=1
        elif ataque[i]-defesa[i+n]<0:
            cont_derrotas+=1
    n+=1
    if cont_derrotas<cont_vitorias:
        confirmacao_venceu=1
        break

# Saída de dados

if confirmacao_venceu==1:
    print('Vitória posicionando as tropas a partir da posição {}'.format(n))
else:
    print('Derrota')


