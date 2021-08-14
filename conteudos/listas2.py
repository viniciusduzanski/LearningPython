teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()

#galera.append(teste)
galera.append(teste[:])

teste[0] = 'Maria'
teste[1] = 22

#galera.append(teste)
galera.append(teste[:])

print(galera)

# ATENÇÃO !!! Não vai ter duas listas, uma com Gustavo 40 e outra com Maria 22.
# AMBOS VÃO SER MARIA 22
# Isso acontece porque no meu primeiro galera.append(teste) eu já criei uma LIGAÇÃO ENTRE AS DUAS ESTRUTURAS, então se eu mudar a primeira estrutura teste, também mudara a estrutura galera.

# Para isso não acontecer, preciso fazer uma cópia, pode ser com: [:] ou .copy()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------


# Também posso declarar uma lista composta da seguinte maneira:
print() # Quebra de linha

              #0   #1       #0   #1       #0      #1      #0     #1
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
                 #0            #1             #2             #3


print(galera2[0]) # Irá mostrar João 19

print(galera2[0][0]) # Irá mostrar somente João

print(galera2[2][1]) # Irá mostrar somente Ana

print(galera2[3][1]) # Irá mostrar 45

print()

for p in galera2:
    #print(p[0]) # Vai imprimir somente os nomes
    #print(p[1]) # Vai imprimir somente as idades
    print(f'{p[0]} tem {p[1]} anos de idade.')

print()

pessoas = list()
dado = list()
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    #galera.append(dado[:]) # Cria uma cópia na lista galera. Não posso esquecer da cópia [:], senão, no comando abaixo, por dado e pessoas estarem ligadas, irá limpar as duas listas.
    pessoas.append(dado.copy()) # A cópia também poderia ser assim.
    dado.clear() # Apaga a informação a cada vez que faz o laço.

print(pessoas)

print()

for p in pessoas:
    if p[1] >= 21:   # p[1] vai pegar a idade
        print(f'{p[0]} é maior de idade.')   # p[0] vai pegar o nome
    else:
        print(f'{p[0]} é menor de idade.')