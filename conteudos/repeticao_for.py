'''
for c in range(0,10):   # Na contagem, ele NÃO CONSIDERA o último número, por isso comecei com 0. Também poderia ser range(1,11)
    print(c, 'Vinícius Duzanski')
print('\n')

# Contar de trás para frente:

for c in range (5, 0, -1):
    print(c)
print('\n')

# Contar pulando números:

for c in range (0, 7, 2):
    print(c)


n = int(input('Digite um número: '))
for c in range(1, n+1):
    print(c)


# Digitar início, onde quer acabar a contagem e pulando de quantos em quantos:

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo :'))
for c in range(i, f+1, p):
    print(c)
'''

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n   # s = s + n
print('O somatório de todos os valores foi {}'.format(s))