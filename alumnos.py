class alumno:

   def registro(self,nombre,calificacion):
       self.nombre=nombre
       self.calificacion=calificacion
       pass

   def AoR(self):
       if self.calificacion >= 6:
           print("el alumno es aprobado")

       else: print("el alumno es reprobado")

   def P(self):

       print("nombre:", self.nombre)

       print("calificacion:", self.calificacion)

A1= alumno()
A2= alumno()

A1.registro("Andony",8)
A2.registro("ana",5)

A1.P()
A1.AoR()
A2.P()
A2.AoR()

