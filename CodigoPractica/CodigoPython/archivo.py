
#Abrir un Archivo
miArchivo = open('miArchivo.txt', 'w')

#Obtener info del archivo
print('Name: ', miArchivo.name)
print('Esta cerrado: ',miArchivo.closed)
print('Esta abierto: ',miArchivo.mode)

#Escribir algo en el archivo

miArchivo.write('Holiwis')
miArchivo.write(' uwu')
miArchivo.close()

#AGregar al Archivo
miArchivo = open('miArchivo.txt', 'a')
miArchivo.write(' bye uwu')

#Leer un archivo
miArchivo = open('miArchi.txt'), 'r+')
texto = miArchivo.read(100)
print(texto)
