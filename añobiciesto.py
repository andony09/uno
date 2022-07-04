def annobisiesto():
  anno: int = int(input("Introduce un año y vamos a ver si es bisiesto "))

  if(anno % 4 == 0 and (anno % 100 != 0 or anno % 400 == 0)):
      print(f"¡El año {anno} es bisiesto!")
  else:
      print(f"Lo sentimos, el año {anno} no es bisiesto!")

print({annobisiesto()})
