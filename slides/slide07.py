
localizacao = {
    'lat': -22.7864,
    'long': -47.8432
}
print(type(localizacao), localizacao)

perfil = {
    'nome': 'Malcolm',
    'idade': 20
}
print(perfil['nome'])
print('nome' in perfil) #verifica se tem essa categoria no dicionario
print(perfil.get('nome')) # retorna o conteudo que está na categoria nome
print(len(perfil)) # retorna o numero de categorias

perfil['cidade'] = 'Osasco' # criando uma nova categoria e adicionando informação
perfil['nome'] = 'Vanessa' # atualizando informações

cidade = perfil.pop('cidade') #tirando a categoria do dicionario e arquivando em um objeto
print(cidade)
print(perfil)
del perfil['nome']
print(perfil)


carro = {
    "Modelo": "Gol",
    "Ano": 2019
}
carro.popitem() #removendo a ultima categoria do dicionario

#ligando um dicionario em outro juntando o que tem em comum
dic_a = {"A": "Avião", "B": "Barco"}
dic_b = {"B": "Balão", "C": "Carro"}
dic_a.update(dic_b)
print(list(dic_a.keys()))
print(list(dic_a.values()))
print(list(dic_a.items()))
print(dic_a)

for automovel in dic_a.values():
    print('Vamos ao passeio de', automovel)

for (letra, automovel) in dic_a.items():
    print('O automóvel', automovel, 'começa com a letra', letra)



####EXERCICIO
dados = [
    {"dia": 12, "mes": 2, "ano": 2019, "temp": 30.5},
    {"dia": 18, "mes": 3, "ano": 2019, "temp": 29.1},
    {"dia": 22, "mes": 4, "ano": 2019, "temp": 28.5},
    {"dia": 17, "mes": 5, "ano": 2019, "temp": 26.4}
]

for i in range(len(dados)):
    dados1 = dict(dados[i])
    values = list(dados1.values())
    i = len(values)
    print('{}/{}/{}: Temperatura: {}C'.format(values[i-4], values[i-3], values[i-2], values[i-1]))


pessoas = ["Alice", "Beatriz", "Carlos"]
telefones = ["99999-0000", "99999-1111", "99999-2222"]
contatos = dict(zip(pessoas , telefones))
print(contatos)
    
pessoas = dict()
n = int(input('Digite o número de pessoas os quais os dados serão inseridos'))
for i in range(n):
    nome = input()
    idade = int(input())
    sexo = input()
    pessoas[nome] = [idade, sexo]

print(pessoas)


