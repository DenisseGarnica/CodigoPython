
# VAlidador de correo
import validador
from validador import validate_email

#Mayoria de edad
x=18


#Clase Usuario
class Usuario:
 def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
#Solicitud del cliente
 def saludos(self):
        return 'Me llamo {0} y tengo {1}. Quisiera hacer una cuenta cliente.'.format(self.nombre, self.edad)
 def tengo_cumple(self):
        self.edad+=1

#Verificacion del correo
 def correo(self):
        if validate_email(self.email):
                print('Tu correo es valido. Bienvenido Usuario')
        else:
             	print('Tu correo no es valido')





#INtroducir datos de Usuario
nombre = raw_input('Introduce tu nombre: ')
print 'Hola: {0} '.format(nombre)

edad = input('Introduce tu edad: ')

if edad<x:
	print('Tienes {0}, por lo tanto puedes ser cliente'.format(edad))

else:
	
	correo = raw_input('Introduce tu correo: ')


	#Definicion de Usuario
	U1 = Usuario(nombre, correo, edad)
	print U1.saludos()
	print U1.edad_cliente()


