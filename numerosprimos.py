def numeroprimo():
  numerop: int = int(input('Introduzca un numero entero: '))

  if numerop > 1:
    # Buscamos los factores de número
    for x in range(2,int(numerop)):
        if (int(numerop) % x) == 0:
            print(f"Lo siento, el número {numerop} NO ES PRIMO. Es divisible entre {x}")
            break
        else:
            print(f"¡ENHORABUENA!, el número {numerop} ES PRIMO")
  else:
    print(f"Lo siento, el número {numerop} NO ES PRIMO. Los números primos son mayores que 1")

print({numeroprimo()})