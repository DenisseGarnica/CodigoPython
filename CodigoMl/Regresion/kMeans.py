#Importar Numpy
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('ggplot') #darle estilo

#Que tipo de machine lerning usaremos
from sklearn.cluster import KMeans

#Preprocesamiento
x = [1,5,1.5,8,1,9]
y = [2,8,1.8,8,0.6,11]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show() #muestra la grafica

#Convierte data a NUmpay array
x = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])

 #Inicializar kMeans
kmeans = KMeans(n_clusters=2)#Define cuantos cluster queremos
kmeans.fit(x)#corre el algoritmo

# Obtener los valores de los centroides
centroids =kmeans.cluster_centers_
labels = kmeans.labels_

print(centroids)
print(labels)
print('*****')
print(type(centroids))
print(type(labels))


colors =["g.","r.","c.","y."]
for i in range(len(x)):
	print('Cordinate: ', x[i], 'Label: ', labels[i])
	plt.plot(x[i][0], x[i],[1], colors[labels[i]], markersize = 10)
	#ESto solo muestra los puntos en el plano

plt.scatter(centroids[:, 0], centroids[:, 1], marker = "x", s=150, linewidths = 5, zorder = 10)

plt.show()
