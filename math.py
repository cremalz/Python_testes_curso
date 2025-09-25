import math
num= int (input ('Digite um numero:'))
raiz = math.sqrt   (num)
print('A raiz quadrada de {} é igual a {}'.format(num, raiz))
print('O valor de {} arredondado para cima é {}'.format(num, math.ceil(raiz)))
print('O valor de {} arredondado para baixo é {}'.format(num, math.floor(raiz)))