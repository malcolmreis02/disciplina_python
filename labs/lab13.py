###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 13 - Eleições 2022
# Nome: Beatriz Donatti
# RA: 247971
###################################################

# Leitura de dados
votos = []
flag = 0
while flag==0:
    voto = input()
    if voto=='0':
        flag+=1
    else:
        votos.append(voto)
lista_candidatos = list(set(votos))
lista_candidatos.sort(reverse=True)
#print(lista_candidatos)

contagem = []
for i in lista_candidatos:
    contagem.append(0)

for i in range(len(lista_candidatos)):
    for j in votos:
        if j ==lista_candidatos[i]:
            contagem[i]=contagem[i]+1
#print(contagem)
'''
for i in range(len(lista_candidatos)):
    if lista_candidatos[i]!='Nulo' and lista_candidatos[i]!='Branco':
        print(lista_candidatos[i], contagem[i])


'''


matriz = dict(zip(lista_candidatos,contagem))
final = []



candi_ordenada = []

for voto in sorted(matriz.values(), reverse= True):
    nome = list(matriz.values()).index(voto)
    if lista_candidatos[nome]=='Branco' or lista_candidatos[nome]=='Nulo':
        continue
    print(lista_candidatos[nome], voto)

ben = [0, 0]
for i in range(len(lista_candidatos)):
    if lista_candidatos[i]=='Branco':
        ben[0] = contagem[i]
    elif lista_candidatos[i]=='Nulo':
        ben[1] = contagem[i]
#print(ben)

print('Brancos', ben[0])
print('Nulos', ben[1])
    





# Saída de dados