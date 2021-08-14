'''

num = [2, 5, 9, 1]
num[2] = 3   # As listas SÃO MUTÁVEIS

# num[4] = 7   # NÃO POSSO ADICIONAR VALORES ASSIM! Preciso utilizar o método APPEND

num.append(7)   # Adiciona o parâmetro ao final da lista

num.sort()   # Organiza em ordem

num.sort(reverse=True)   # Coloca em ordem AO CONTRÁRIO

num.insert(2, 0)   # Na posição 2, vou inserir o valor 0

num.pop()   # Remove o último elemento da lista

num.pop(2)   # Remove o elemento que está no ÍNDICE 2

num.insert(2, 2)   # Na posição 2, vou inserir o valor 0

num.remove(2)   # Eu tenho duas vezes o número 2 na minha lista, se eu mandar ele remover o número 2, ele vai remover o PRIMEIRO 2 da esquerda para direita

if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4.')

print(num)

print(f'Essa lista em {len(num)} elementos.')

'''
##########################################################################################


# Posso criar uma lista assim:

valores = []

# Ou assim:

valores2 = list()

valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')

print('\n')


# Printar o VALOR e o ÍNDICE da lista:

for c, v in enumerate(valores):   # A função enumerate pega TANTO a chave quanto o valor
    print(f'Na posição {c} encontrei o valor {v}.')
print('Cheguei ao final da lista.')


# Usuário acrescentando valores na lista:

for cont in range(0, 5):
    valores2.append(int(input('Digite um valor: ')))
print(valores2)

#################################################################################

'''
ATENÇÃO !!! Quando eu igualo uma lista à outra, e faço uma alteração em alguma dessa lista, ele MEXE NAS DUAS !!!
'''

a = [2, 3, 4, 7]
b = a
b[2] = 8   # Quero colocar o valor 8 no índice 2 APENAS NA POSIÇÃO 2 DA LISTA B, porém, a lista A também será mudada!
print(f'Lista A: {a}')
print(f'Lista B: {b}')

# Solucionando isso:

b = a[:]   # b vai receber uma CÓPIA de a
b[2] = 525
print(f'Lista A: {a}')
print(f'Lista B: {b}')

b = a.copy()   # em vez do jeito acima, posso utilizar o MÉTODO COPY
b[3] = 1000
print(f'Lista A: {a}')
print(f'Lista B: {b}')


print(*b, sep= ', ')# '*' mostra a lista sem os colchetes, e sep é a string entre as variáveis da lista


#################################################################################

'''
Se eu quero SOMENTE OS VALORES da lista:
    - for normal -> for c in valores


Se eu quero os VALORES e o ÍNDICE desses valores da lista:
    - enumerate

    Conheço o tamanho da lista? SIM:
        - range -> for c in range(0, 10) -----------> pegar o índice utilizo o c --------------> pegar o valor utilizo lista[c]

'''