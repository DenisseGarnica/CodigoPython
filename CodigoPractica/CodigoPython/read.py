cadena =input('Ingresa tu nombre: ')
print ('Hola:',cadena)

numero = input('Introduce tu edad: ')

#Clases
class Usuario:
 def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
 def saludos(self):
        return 'Me llamo {0} y tengo {1}'.format(self.nombre, self.edad)
 def tengo_cumple(self):
        self.edad+=1

U1 = Usuario('cadena', 'denisse@gmail.com', numero)
print U1.saludos()

