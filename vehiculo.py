#las tres maneras de poder guardar una variable 
#e imprimirla
miVehiculo = input ("nombre del vehiculo")
print("su vehiculo es un"+ miVehiculo) 
print(f"su vehiculo es un{miVehiculo}")
print("su vehiculo es un{}".format(miVehiculo))
#combinacion de variables
puerta = input ("mete la cantidad de puertas de tu vehiculo aqui: ")
print("su vehiculo es un" + miVehiculo + ", su cantidad de puertas son: " + puerta)
