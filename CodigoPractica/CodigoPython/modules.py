#Modulos

#Forma 1
import datetime
hoy = datetime.date.today()
print(hoy)

#Forma 2
from datetime import date
hoy2 = date.today()
print(hoy2)

import time
estampatemporal = time.time()
print(estampatemporal)

# Modulo personalizado
import validador
from validador import validate_email

email = 'denisse.garnica01gmail.com'
if validate_email(email):
	print('El correo esta bien escrito')
else:
	print('El correo esta mal escrito')
