edad= input ("ponga su edad ")
edad =int (edad) #nos ayuda a definir si es tipo int

if edad >= 18 and edad <= 99:
    print(edad,"eres mayor de edad")
elif edad >=100:
    print(edad,"eres una momia")
elif edad < 18:
    print(edad,",eres menor de edad")
    