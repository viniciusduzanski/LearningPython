'''
for c in range(1, 10):
    print(c)
print('Fim')
'''

# A estrtura while serve para quando eu NÃO SEI O LIMITE e também para quando eu SEI O LIMITE. Já o for, SÓ SERVE QUANDO EU SEI O LIMITE.
# Sei o limite -> posso usar o FOR e o WHILE
# Não sei o limite -> só posso usar o WHILE

c = 1
while c < 10:
    print(c)
    c += 1   # c = c + 1
print('Fim')

'''
n = 1
while n != 0:   # Eu não conseguiria fazer esse exemplo com o FOR, pois não sei quantos números o usuário vai digitar
    n = int(input('Digite um número: '))
print('Fim')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:   # Para não contabilizar o 0 quando for para sair do while
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares!')