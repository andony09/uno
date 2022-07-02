#calcula tu indice de masa corporal
peso= input("¿cual es tu peso en kg?")
estatura= input("¿cual es tu estatura en metros?")
imc= round(float(peso)/float(estatura)**2,2)
print("tu indice de masa corportal es " + str(imc))
