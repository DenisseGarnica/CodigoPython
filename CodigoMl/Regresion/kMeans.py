#Importar Numpy
numpy as np
import matplotlib.pyplot as plt

from matplotlib import style
style.use('gplot') #darle estilo

#Que tipo de machine lerning usaremos
from sklearn.cluster import kMeans

#Preprocesamiento
x = [1,5,1.5]
y = [2,8, 1.8 ]

print(len(x))
print(len(y))

plt.scatter(x,y)
plt.show() #muestra la grafica

#Convierte data a NUmpay array

x = np.array([[1,2], [5,8], [1.5,1.8]])

 #Inicializar kMeans
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Obtener los valores de los centroides

centroids =kmeans.cluster_centers_
labels = kmeans.labels_
