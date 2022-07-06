class vehiculo:
    carro= True

    def color(self):
        self.carro= "el color del coche es negro"

    def ruedas(self):
        self.carro="el coche tiene 4 ruedas"

    def puertas(self):
        self.carro="el coche tiene 4 puertas"

    def iscarro(self):
        return self.carro;

class coche(vehiculo):
    velocidad= None
    cilindrada= None
    def __init__(self):
        self.velocidad= "corre a 200km/h"
        self.cilindrada= "8 cilindros"

    def iscarro(self):
        pass
v= vehiculo()
v.color()
print(v.iscarro())
v.ruedas()
print(v.iscarro())
v.puertas()
print(v.iscarro())
v= coche()
print(v.velocidad)
print(v.cilindrada)
