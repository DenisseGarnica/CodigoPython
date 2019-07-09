#Condicionales

x=10
y=5

if x>y:
	print('{0} es mas grande que {1}'.format(x,y))
elif x==y:
	print('{0} y {1} son iguales'.format(x,y))
else:
	print('{1} es mas grande que {0}'.format(x,y))

if x>2:
 if x<=10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

numbers = [1,2,3,4,5]
z = 5

#AND
if x > 2 and x <= 10:
	print('{0} es mas grande que 2 e igual/menor a 10'.format(x))

#OR
if x > 2 or x<=10:
	print('{0} es mas grande que 2 e igual/menos a 10'.format(x))

if not(x==y):
	print('{0} no es igual a {1}'.format(x,y))
