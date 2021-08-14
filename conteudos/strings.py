frase = 'Curso em Vídeo Python'

print(frase[3])   # Indexador 3, vai mostrar a 4ª letra, pois começa em 0.

print(frase[3:13])   # Começa no indexador 3 e vai até o 13, só que NÃO MOSTRA O 13, ou seja, vai da 4ª letra até a 14ª letra, mas não irá imprimir a 14ª, só até a 13ª

print(frase[:13])

print(frase[13:])

print(frase[1:15:2])

print(frase[1::2])

print(frase[::2])

print(frase.count('o'))

print(frase.count('O'))

print(frase.upper().count('O'))   # Transformo toda a frase em letras maiúsculas e depois conto a quantidade de O maiúsculo nela

print(len(frase))

print(frase.replace('Python', 'Android'))   # Ele não substitui de MANEIRA DEFINITIVA. Vai substituir somente nessa instância. Se eu fazer um novo print de frase, ainda vai ser python.

print(frase)

frase = frase.replace('Python', 'Android')

print(frase)

print('Curso' in frase)   # Vai retornar TRUE ou FALSE. 

print(frase.find('Curso'))   # Vai retornar a POSIÇÃO de onde começa a palavra curso, nesse caso vai ser 0.

print(frase.find('vídeo'))   # O Python diferencia minúscula de maiúscula, então quando o find não encontra, ele retorna -1

print(frase.lower().find('vídeo'))   # Agora vai aparecer, pois estou deixando a string inteira em minúsculo antes de fazer o find

print(frase.split())   # Vai dividir a frase em palavras na quantidade de espaço que existe entre elas, criando uma lista

dividido = frase.split()

print(dividido[2][3])   # Como foi criado uma lista na variável dividido, nesse comando estou imprimindo a terceira letra da palavra que está na posição 2 da lista (Vídeo)

# Usando aspas 3 vezes para imprimir um texto grande:

print("""Guido Van Rossum criou o Python em 1989.
Ele trabalhava no Centrum Voor Wiskunde en Informatica no início dos anos 1980,
e seu trabalho era implementar
a linguagem de programação conhecida como ABC.
... Esta primeira versão tinha um sistema de módulo Modula-3,
linguagem que foi posteriormente denominada “Python”.""")