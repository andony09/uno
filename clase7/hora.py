# Importamos el módulo time para poder obtener la hora.
import time

# Iniciamos las variables y formateamos el tiempo para que solo se vean las horas y minutos
# %H = Hora (reloj de 24 horas) como un número decimal [00,23].
# %M = Minuto como número decimal [00,59].

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora) >= 19:
    print ("Es hora de irnos a casa")
else:
    print ("Quedan {} horas y {} minutos para retirarse a casa".format(18- int(hora), 59-int(minutos)))
