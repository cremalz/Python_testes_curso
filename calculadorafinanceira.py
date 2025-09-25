print ('Ola bem vindo a sua calculadora financeira')
v=float(input('Em qual valor você quer chegar :' ))
n1=float(input('Qual seria sua renda mensal :')) 
n2=float(input('Qual seria seu gasto mensal :'))
n3=float(n1-n2)
p=float(input('Quanto dinehiro você tem guardado:'))
p1=(n3+p)

print('levando emconcideração que seu salario é {} seu gasto {} suarenda mensal é de {}  '.format(n1,n2,n3))
print('sua meta é chegar em  {} e que você ja tem {} você demoraria {}meses para concretizar sua meta '.format(v,p,p1/v))







