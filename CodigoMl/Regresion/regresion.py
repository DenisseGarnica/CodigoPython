#Import
import matplotlib.pyplot as plt
import numpy as np

#importing from scikit-learn
from sklearn import datasets, linear_model

#load dataset
house_price = [245,321,279,308,199,219,405,324,319,255]
size = [1400,1600,1700,1875,1100,1550,2350,2450,1425,1700]

print(len(house_price))
print(len(size))

#Reshape the input to your regression
size2 = np.array(size).reshape((-1,1)) #Aqui usa el numpy para que ordene los datos de 1 en 1. 
					#No puede ordenarlo en un numoer que no sea divisible al tamano

print(size2)

#by using fit module in linear regresion, user can fit the data fast
regr = linear_model.LinearRegression()
#clase
regr.fit(size2, house_price)
print('Coeficientes: {0}'.format(regr.coef_))
print ('Intersecciones: {0}'.format(regr.intercept_))

#Formula obtenida por el modelo
def graph(formula, x_range):
	x = np.array(x_range)
	y = eval(formula)
	plt.plot(x,y)

#PLotting the prediction line
graph('regr.coef_*x + regr.intercept_', range(500,2000)) #esto para visualizar
plt.scatter(size, house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
plt.show()
