def soma(a, b):   # Declaração da função
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')


soma(4, 5)   # Passo 4 e 5 como parâmetro para a função
soma(b=3, a=8)   # Nesse caso eu inverti a ordem, para isso, eu PRECISO EXPLICITAR qual é qual variável

def contador(*num):   # Vai receber os dados como tuplas, então posso utilizar todos os recursos de tupla
    for valor in num:
        tam = len(num)
        print(f'Recebi os valores {num} e são ao todo {tam} números')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

#----------------------------------------------------------------------------------------------

print()

def dobra(lst):   # Cria a função e recebe por parâmetro a lista valores, mas aqui dentro da função ela será reconhecida por lst. NÃO É DESEMPACOTAMENTO!
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2   # Multiplica por 2 cada elemento da lista / tudo que eu fizer em lst vai alterar em valores. Aqui eu NÃO ESTOU DESEMPACOTANDO!
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)   # Chama a função passando a lista por parâmetro
print(valores)


# Desempacotamento:

def soma2(*val):   # Desempacotamento
    s = 0
    for num in valores:
        s+= num
    print(f'Somando os valores {valores} temos {s}')

soma2(5, 2)
soma2(2, 9, 4)