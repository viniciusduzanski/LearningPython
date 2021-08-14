pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print()

print(pessoas.keys())   # Vai mostrar as chaves do dicionário -> nome, sexo e idade -> Vai imprimir no formato de LISTA
print(pessoas.values())   # Vai mostrar os valores do dicionário -> Gustavo, M e 22 -> Vai imprimir no formato de LISTA
print(pessoas.items())   # Vai mostrar os itens, ou seja, a combinação das chaves e valores -> Vai imprimir no formato de TUPLAS dentro de uma LISTA

print()

for k, v in pessoas.items():
    print(f'{k} = {v}')

print()

del pessoas['sexo']   # Vai apagar o item sexo

pessoas['nome'] = 'Vinícius'   # Substituir um elemento

pessoas['peso'] = 80   # Adicionar um elemento

#---------------------------------------------------------------------------------------------#
print()
# Dicionários dentro de uma lista:

brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)

print()

print(brasil[0])   # Vai mostrar o que foi adicionado primeiro, no caso vai mostrar o dicionário que se refere à Rio de Janeiro
print(brasil[1])   # Vai mostrar o dicionário que se refere à São Paulo
print(brasil[0]['uf'])   # Vai mostrar Rio de Janeiro

print()

estado = dict()
brasil2 = list()
for c in range(0, 3):   # Cadastrar 3
    estado['uf'] = str(input('Unidade Federativa: '))   # uf vai ser a chave, e o que ele ler de unidade federativa vai ser o valor
    estado['sigla'] = str(input('Sigla do Estado: '))   # sigla vai ser a chave, e o que ele ler de sigla do estado vai ser o valor
    brasil2.append(estado.copy())   # Se eu não fizer a cópia vai criar relação com o dicionário e vai dar problema. Preciso usar o método copy(). O fatiamento [:] NÃO DÁ CERTO!
print(brasil2)

print()

for e in brasil:   # Percorre a LISTA
    for v in e.values():   # Percorre os VALORES do dicionário. Precisa ser e.values() e não somente values() porque o e estará recebendo tanto a chave quanto o valor do dicionário quando ele passar pelos elementos da lista
        print(v, end=' ')