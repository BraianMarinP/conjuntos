class Operaciones():
   def Union(self):
       print("Se ha seleccionado la opción 1.")
       for elemento in conjunto2:
           conjunto1.append(elemento)
       print(conjunto1)


   def Interseccion(self):
       print("Se ha seleccionado la opción 2.")
       conjuntoInterseccion = []
       for elemento in conjunto2:
           if elemento in conjunto1:
               conjuntoInterseccion.append(elemento)
       print(conjuntoInterseccion)


   def Diferencia(self):
       print("Se ha seleccionado la opción 3.")
       for elemento in conjunto2:
           if elemento in conjunto1:
               conjunto1.remove(elemento)
       print(conjunto1)


   def Complemento(self):
       print("Se ha seleccionado la opción 4.")
       conjuntoComplemento = []
       for elemento in conjunto2:
           if elemento not in conjunto1:
               conjuntoComplemento.append(elemento)
       print(conjuntoComplemento)




   def Combinacion(self):
       print("Se ha seleccionado la opción 5.")


   def default_case(self):
       print("Opción no válida.")


operaciones = Operaciones()
conjunto1 = []
conjunto2 = []


switch = {
       1: operaciones.Union,
       2: operaciones.Interseccion,
       3: operaciones.Diferencia,
       4: operaciones.Complemento,
       5: operaciones.Combinacion
   }


while True:
   entrada = input("Ingrese un elemento para el primer conjunto (end; para terminar): ")
   if entrada == "end;":
       break;
   else:
       conjunto1.append(entrada)


while True:
   entrada = input("Ingrese un elemento para el segundo conjunto (end; para terminar): ")
   if entrada == "end;":
       break;
   else:
       conjunto2.append(entrada)


print(conjunto1)
print(conjunto2)


operacion = input("Ingrese una opción:"
                     "\n 1. Union"
                     "\n 2. Interseccion"
                     "\n 3. Diferencia"
                     "\n 4. Complemento"
                     "\n 5. Combinación entre ellos"
                     "\n 6. Salir")


opcionSeleccionada = switch.get(int(operacion))
opcionSeleccionada()




    













































