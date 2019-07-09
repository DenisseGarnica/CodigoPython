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

Morra = Usuario('Denisse', 'denisse@gmail.com', 17)
print Morra.saludos()
print(type(Morra))
print(Morra.nombre)

#Extender Clases
class Cliente(Usuario):
 def __init__(self, nombre, email, edad):
	self.nombre = nombre
	self.email = email
	self.edad = edad
	self.saldo = 0
 def establecer_saldo(self,saldo):
	self.saldo = saldo
 def saludos(self):
	return 'Me llamo {0}, tengo {1} y mi saldo es {2}'.format(self.nombre, self.edad, self.saldo)

#INit un objeto del tipo Usuario
Chispita_usuario = Usuario('Chispita', 'chispita@gmail.com', 8)
print type(Chispita_usuario)
print Chispita_usuario.nombre
print Chispita_usuario.saludos()

Chispita_cliente = Cliente('Chispi', 'chispi@gmail.com', 8)
Chispita_cliente.establecer_saldo(5e10)
print Chispita_cliente.saludos()
print Chispita_usuario.saludos()

