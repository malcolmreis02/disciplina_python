###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Ingresso do Cinema
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
# Link do enunciado: https://susy.ic.unicamp.br:9999/mc102/03/enunciado.html
###################################################

# leitura de dados
dia_semana = int(input())
horas_sessao = int(input())
minuto_sessao = int(input())
condicao_estudante = str(input())
met_pagamento = str(input())

# valor do ingresso inteiro

precos_dia = [30, 15, 15, 15, 20, 20, 30]
precos_noite = [30, 20, 20, 30, 30, 40, 40]
desconto_cred_dia = [0.3, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2]
desconto_cred_noite = [0.3, 0.5, 0.5, 0.5, 0.5, 0.3, 0.2]

# valor a pagar

if (horas_sessao>=18 and minuto_sessao>=30) or horas_sessao>=19:
    ingresso = precos_noite[dia_semana-1]
    if condicao_estudante=='S':
        ingresso = ingresso*0.5
    elif met_pagamento=='C':
        ingresso = ingresso - (ingresso*desconto_cred_noite[dia_semana-1])
else:
    ingresso = precos_dia[dia_semana-1]
    if condicao_estudante=='S':
        ingresso = ingresso*0.5
    elif met_pagamento=='C':
        ingresso = ingresso - (ingresso*desconto_cred_dia[dia_semana-1])



# saída do valor do ingresso
print('Valor do ingresso: R$', format(ingresso, '.2f').replace('.', ','))


#rascunho
'''
<Dia da semana>(1, 2, 3, 4, 5, 6, 7) sendo 1 domingo, 2 segunda, ...
<Hora de início da sessão>
<Minuto de início da sessão>
<Estudante>(S/N) sim ou nao
<Método de pagamento>(D/C) dinheiro ou cartao

ex:
2
19
15
S
C
'''