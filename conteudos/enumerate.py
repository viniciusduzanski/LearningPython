# Permite iterar sobre uma lista sem a necessidade de declarar um contador e ficar incrementando ele

lista_nomes = ['Vinícius', 'João', 'Pedro', 'Ronaldo', 'Jucilene', 'Cumpadi']
for indice, nomes in enumerate(lista_nomes):
    print(f'Na posição {indice} está escrito {nomes}.')