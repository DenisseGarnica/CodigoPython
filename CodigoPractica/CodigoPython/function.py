#Funciones

#Funcion Saludar
def decirHola(nombre=''):
	print('Hola {0}'.format(nombre))
decirHola('Chispita')
decirHola()


#Funcion Suma
def hacerSuma(num1, num2):
	total = num1 + num2
	return float(total)
print(hacerSuma(2,56), type(hacerSuma(2,56)))

x = 2
y = 2
total = hacerSuma(x,y)
print(total, type(total))
