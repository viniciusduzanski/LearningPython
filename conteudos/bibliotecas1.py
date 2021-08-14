# import math
from math import sqrt, ceil
num = int(input('Digite um número: '))
# raiz = math.sqrt(num) // Utilizaria assim se eu importasse a biblioteca toda
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, ceil(raiz)))
