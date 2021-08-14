# Duas maneiras de pesquisar:
'''
help()   # Depois vou precisar digitar print lá no terminal
help(print)   # Já vai mostrar direto sobre o print
'''

############################## CRIANDO DOCSTRINGS ##############################

def contador(i, f, p):
    """
    -> Faz uama contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    Função criada por Vinícius Duzanski assistindo as aulas do Curso em Vídeo.
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM')

help(contador)   # Vefico a docstring da função contador.


############################## PARÂMETROS OPCIONAIS ##############################

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(3, 2, 5)   # Chamei a função sem problemas, pois ela foi definida como 3 parâmetros e chamei ele também com 3 parâmetros.
somar(3, 2)   # Não defini o valor de c, por isso precisei deixar ele como opcional lá em cima na função, definindo ele como 0. c=0
somar(3)   # Preciso deixar o parâmetro b lá na função como parâmetro opcional também.
somar()   # Para isso, preciso deixar todos os parâmetros como opcionais.

# Lembrando que para os casos acima SÓ POSSO 3 PARÂMETROS. Se fosse para passar mais de 3 precisaria passar como tupla, lista ou empacotado (colocando o asterisco)