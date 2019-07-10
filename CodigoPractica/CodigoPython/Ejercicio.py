# Modulo personalizado
import validador
from validador import validate_email


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

#Se verifica la edad del cliente
 def edad_cliente(self):
	if self.edad>=x:
		print('Tienes {0}, por lo tanto puedes ser cliente'.format(self.edad))
	else: 	
		print('Tienes {0}, por lo tanto NO puedes ser cliente'.format(self.edad))
#Verificacion del correo
 def correo(self):
	if validate_email(self.email):
        	print('Tu correo es valido. Bienvenido Usuario')
	else:
     		print('Tu correo no es valido')




Quetzalli = Usuario('Quetzalli', 'quetzalli@gmail.com', 17)
print Quetzalli.saludos()
print Quetzalli.edad_cliente()

Ana = Usuario('Ana', 'Anagmail.com', 21)
print Ana.saludos()
print Ana.edad_cliente()
print Ana.correo()

Gabriel = Usuario('Gabriel', 'gabriel@gamil.com', 32)
print Gabriel.saludos()
print Gabriel.edad_cliente()
print Gabriel.correo()



#ClaseCliente
class Cliente(Usuario):
 def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        self.saldo = 0
 def establecer_saldo(self,saldo):
        self.saldo = saldo
 def saludos(self):
        return 'Me llamo {0}, soy cliente, tengo {1} y mi saldo es {2}'.format(self.nombre, self.edad, self.saldo)
 def bancarrota(self):
	while self.saldo>0:
		print('Has gastado 200 pesos')
		self.saldo=self.saldo-200
		print('Tu nuevo saldo es {0}'.format(self.saldo))
	if self.saldo==0:
		print('Tu saldo es 0, estas en bancarrota')


#Gabriel Cliente
Gabriel_cliente = Cliente('Gabriel', 'gabriel@gmail.com', 32)
Gabriel_cliente.establecer_saldo(5000)
print Gabriel_cliente.saludos()
print Gabriel_cliente.bancarrota()


