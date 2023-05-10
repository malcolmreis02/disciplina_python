###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Controle de Estoque
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
###################################################

# leitura da sequência de compras e vendas
seq = list()
estoque = 0
contagem_vendas = 0

while True:
    mov = int(input())
    seq.append(mov)
    if mov==0:
        break

for i in seq:
    #comprando para o estoque
    if i>0:
        estoque = estoque + i

    #fazendo a venda (tirando do estoque)
    elif i<0:
        i = -i
        if i>estoque:
            print('Quantidade indisponível para a venda de {} unidades.'.format(i))
        else:
            estoque = estoque - i
            contagem_vendas = contagem_vendas + 1


# impressão da saída

    
print('Quantidade de vendas realizadas: {}'.format(contagem_vendas))
print('Quantidade em estoque: {}'.format(estoque))


# rascunho

'''
x positivo = compra de produtos para estoque
y negativo = venda de produtos
'''