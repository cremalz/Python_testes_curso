num = int(input('Digite um numero: '))
n= str(num)
print('analisando o numero {}'.format(num))
print('unidade: {}'.format(n[3]))
print('dezena: {}'.format(n[2]))
print('centena: {}'.format(n[1]))
print('milhar: {}'.format(n[0]))

ud= num // 1 % 10
de= num // 10 % 10 
ce= num // 100 % 10
mi= num // 1000 % 10
print('unidade: {}'.format(ud))
print('dezena: {}'.format(de))
print('centena: {}'.format(ce))
print('milhar: {}'.format(mi))

