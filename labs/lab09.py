###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Controle de Estoque 2.0
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
###################################################

# Leitura de dados
estoque = {}
pcompras = {}
pvendas = {}
movimentacao = []
flag=0

while flag==0:
    teste = input()
    if teste=='FIM':
        flag=1
    else:
        dados = teste.split(' : ')
        movimentacao.append(dados)

for i in movimentacao:
    estoque[i[0]]=0
    pcompras[i[0]]=0
    pvendas[i[0]]=0

# Processamento

for i in movimentacao:
    mov = int(i[1])
    if mov<0:
        if -mov>estoque.get(i[0]):
            print("Quantidade indisponivel para a venda de {} unidade(s) do produto {}.".format(-mov, i[0]))
        else:
            pvendas[i[0]]+=1
            estoque[i[0]]=estoque.get(i[0])+mov
    else:
        pcompras[i[0]]+=1
        estoque[i[0]]=estoque.get(i[0])+mov

ordem = []
for i in movimentacao:
    ordem.append(i[0])
sorted(ordem)

nomes = []
for i in movimentacao:
    nomes.append(i[0])
nomes2 = list(sorted(set(nomes)))

# Impressão da saída

for i in nomes2:
    if estoque[i]!=0 or pcompras[i]!=0 or pvendas[i]!=0:
        print("Produto: " + i)
        print("Quantidade em Estoque: {}".format(estoque[i]))
        print("Pedidos de Compra: {}".format(pcompras[i]))
        print("Pedidos de Venda: {}".format(pvendas[i]))




