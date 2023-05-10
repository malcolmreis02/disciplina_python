##################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - Jornada de Trabalho
# Nome: Malcolm dos Reis Alves Pereira
# RA: 187642
##################################################

# Leitura do valor da hora
v = int(input())

# Leitura do numero de dias trabalhados na semana
d = int(input())

# Leitora e processamento dos periodos de trabalho de cada dia
lista_periodos = list()
for i in range(d):
    vezes = int(input())
    lista_periodos.append(vezes)
    for i in range(vezes*2):
        lista_periodos.append(int(input()))

lista_carga_horaria = list()
for i in range(d):
    lista_diaria = list()
    for j in range(lista_periodos[0]):
        horas_trabalhadas = lista_periodos[2] - lista_periodos[1]
        lista_diaria.append(horas_trabalhadas)
        lista_periodos.pop(1)
        lista_periodos.pop(1)
    lista_carga_horaria.append(sum(lista_diaria))
    lista_periodos.pop(0)

horas_trabalhadas = sum(lista_carga_horaria)

lista_horas_extra = list()
for i in lista_carga_horaria:
    if i>8:
        lista_horas_extra.append(i-8)


# Calculo do valor devido ao funcionário
if sum(lista_carga_horaria)>44 or len(lista_horas_extra)>0:
    horas_extra_dia = sum(lista_horas_extra)

    if sum(lista_carga_horaria)-horas_extra_dia>44:
        horas_extra_todo = ((sum(lista_carga_horaria)-horas_extra_dia)-44)
        horas_extras = horas_extra_dia+horas_extra_todo
    else:
        horas_extras = horas_extra_dia
else:
    horas_extras = 0

valor = v*horas_trabalhadas + v*horas_extras*0.5

# Impressão da saída

print("Horas trabalhadas:", horas_trabalhadas)
print("Horas extras:", horas_extras)
print("Valor devido: R$ {:0.2f}".format(valor))
