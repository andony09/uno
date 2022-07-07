#ciclo if
print("iniciamos ciclo if")
numero=5
if numero > 0:
    print("el numero es positivo")
elif numero == 0:
    print("el numero es igual a cero")

else:print("el numero es negativo")

#ciclo while
print("iniciamos switch")
numero= 1
while numero <=10:
    print("numero vale",numero)  #lo que sucede dentro del while se le llama iteracion
    numero+= 1

#aplicandole un break
print("iniciamos el switch pero para que se aplique una vez")
numero= 4
while numero <=10:
    print("numero vale",numero)  #lo que sucede dentro del while se le llama iteracion
    numero+= 1
    break

#ciclo for
print("iniciamos con el ciclo for")
for i in range (0,21):
    print(i)

#switch
print("iniciamos el switch")
estacion= "otoño"
match estacion:
    case "primavera":
        print("estamos en primavera")
    case "verano":
        print("estamos en verano")
    case "otoño":
        print("estamos en otoño")
    case "invierno":
        print("estamos en invierno")