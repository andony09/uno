puerta = input("mete la cantidad de puertas de tu vehiculo:")

puerta = int (puerta)#esto es un casteo o parcearlo para que nos de un entero

if puerta <= 3:
   print("te hacen falta puertas")
elif puerta >= 4 and puerta <= 5:
    print("tu vehiculo esta completo")
else:
    print("ponga un numero del 1 al 8 real")

