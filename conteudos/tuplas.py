lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

# Manipulação das Tuplas:   mesmos conceitos das strings

print(lanche[1])   # Vai imprimir Suco, pois Hambúrguer é a posição 0.
print(lanche[-2])   # Vai imprimir Pizza, pois começa do final para o início, onde o -1 é o Pudim.
print(lanche[1:3])   # Lembre-se que o Python NÃO É INCLUSIVO À DIREITA, ou seja, o índice 3 não será contabilizado. Vai imprimir Suco e Pizza.
print(lanche[-3:])   # Vai imprimir Suco, Pizza e Pudim.

### TUPLAS SÃO IMUTÁVEIS!!! ### Não posso alterar qualquer posição, ex: lanche[1] = 'Refrigerante'



########################################################### 3 MANEIRAS DE ITERAR UMA TUPLA ########################################################

# Aqui NÃO CONSIGO mostrar a posição da tupla

for comida in lanche:   # Próprio Python cria uma variável simples chamada comida para iterar na tupla.
    print(f'Eu vou comer {comida}.')   # Comida vai assumir o valor de cada posição conforme vai sendo iterado. Primeiro vai receber hambúrguer, depois suco, depois pizza e por último pudim.
print('Comi pra caramba!')


# Utilizando range e len para iterar a tupla:
# Aqui eu posso mostrar a POSIÇÃO DA TUPLA

for cont in range(0, len(lanche)):   # Lembre-se que o range também ignora o último valor. Por mais que o len retorne 4, ele só irá ir até 3.
    print(lanche[cont])   # Imprimir o item da tupla na posição que cont assume, pois cont vai assumir apenas os valores inteiros 0, 1, 2 e 3.


# Utilizando ENUMERATE: posso conseguir a posição da tupla

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')   # pos vai iterar entre 0, 1, 2 e 3. comida vai iterar entre hambúrguer, suco, pizza e pudim

##################################################################################################################################################


print(sorted(lanche))   # Coloca a tupla em ordem alfabética. Vai imprimir uma LISTA. Mas NÃO ALTERA a tupla.


a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b   # Vai CONCATENAR as tuplas, ou seja, vai imprimir: (2, 5, 4, 5, 8, 1, 2)
print(c)


print(c.count(5))   # Utilizando método na própria tupla. Quantas vezes aparece o elemento 5 nesse tupla?


print(c.index(8))   # Em que posição está o elemento 8? Em que índice. Se fosse um texto, também poderia ser

print(c.index(5, 2))   # Tenho 2 índices que contém o elemento 5, ele vai mostrar a PRIMEIRA OCORRÊNCIA. Nesse caso, ele vai mostrar qual posição está aquele outro 5, a partir da posição 2.


pessoa = ('Vinícius', 22, 'M', 88.50)   # Posso colocar tanto letras como também números

del(pessoa)   # Apaga a tupla