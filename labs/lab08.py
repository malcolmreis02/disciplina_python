###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Wordle
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
###################################################

# Leitura da palavra
palavra = input()
lista_palavra = list()
for i in palavra:
    lista_palavra.append(i)


# Leitura dos palpites e impressão do resultado para cada palpite
acertou = 0
n=0
retornos = list()
palpites = list()

for i in range(6):
    palpite = input()
    palpites.append(palpite)
    if palpite==palavra:
        break


for n in palpites:
    lista_palpite = list()
    retorno_palpite = list()
    for j in n:
        lista_palpite.append(j)

    for i in range(len(lista_palavra)):
        if palavra[i]==n[i]:
            lista_palpite[i] = lista_palpite[i].upper()
        elif n[i] not in lista_palavra:
            lista_palpite[i] = '_'
        retorno_palpite.append(lista_palpite[i])
    retorno_palpite_str = ''.join(retorno_palpite)
    retornos.append(retorno_palpite_str)
    if retorno_palpite_str==palavra:
        acertou+=1


for i in retornos:
    print(i) 

if palavra.upper() not in retornos:
    print('Palavra correta:', palavra)
else:
    print('Resposta correta')     
