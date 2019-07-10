#Import
import matplotlib.pyplot as plt
import numpy as np

#importing from scikit-learn
from sklearn import datasets, linerar_model

#load dataset
house_price = [245, 321, 279]
size = [1400, 1600, 1700]

print(len(house_price))
print(len(size))
#Reshape the input to your regression
size2 = np.array(size).reshape((-1,1))

print(size2)

#by using fit module in linear regresion, user can fit the data fast








regr = linear_model.LinearRegresion()
regr.fit(size2, house_price)
print('Coeficients: {0}'.format(regr.coef_))
print('Intercept: {0}'.format(regr.intercept_)

#Formula obtained for the trained model

def graph(formula, x_range):
	x = np.array(x_range)
	y = eval(formula)
	plt.plot(x, y)

#PLotting the prediction line
grap('regr.coef_*x +regr.intercept_', range(500, 3000))
plt.scatter(size,house_price, color='black')
plt.ylabel('house price')
plt.xlabel('size of house')
