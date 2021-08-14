# Utilizando for:

nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    print(nome)

# Utilizando while:

contador = 0
nomes_cidades_2 = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
while contador < len(nomes_cidades_2):   # len retorna quantos itens tem na lista, nesse caso são 4. Então enquanto contador for menor que 4, roda o código. Vai rodar quando contador = 0, contador = 1, contador = 2, contador = 3, assim, irá acessar os 4 itens da lista.
    print(nomes_cidades[contador])
    contador += 1

# Utilizando for com dicionários:

cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes': 12.2
}
for chave in cidade:   # O for em um dicionário, o iterador vai RETORNAR A CHAVE
    print(f'{chave}: {cidade[chave]}')   # Aqui ele vai imprimir a chave e em sequência o VALOR da chave.