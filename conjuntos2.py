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





for elemento in conjuntoA:
    conjuntoUniversal.append(elemento)

for elemento in conjuntoB:
    if elemento not in conjuntoUniversal:
        conjuntoUniversal.append(elemento)

for elemento in conjuntoC:
    if elemento not in conjuntoUniversal:
        conjuntoUniversal.append(elemento)

DiccionarioOperaciones = {

    "1": operador.Union(conjuntoA, conjuntoB, conjuntoC),
    "2": operador.Interseccion(conjuntoA, conjuntoB, conjuntoC),
    "3": operador.Diferencia(conjuntoA, conjuntoB, conjuntoC),
    "4": operador.Complemento(conjuntoA, conjuntoB, conjuntoC, conjuntoUniversal)

}

DiccionarioConjuntos = {

    "A": conjuntoA.copy(),
    "B": conjuntoB.copy(),
    "C": conjuntoC.copy()

}

print("\nU = " + str(conjuntoUniversal))



while True:
    opcion =  input("\nIngrese una opción para operar con los conjuntos: "
                    "\n0. Para representación gráfica."
                    "\n1. Para union."
                    "\n2. Para intersección."
                    "\n3. Para diferencia."
                    "\n4. Para complemento."
                    "\n5. Para combinación."
                    "\n6. Para salir.\n")
    
    if opcion == "0":
        generar_diagrama3()
        #conjuntosGrafico = []
        #venn3([set (conjuntoA), set (conjuntoB), set (conjuntoC)], set_labels=('Conjunto A', 'Conjunto B', 'Conjunto C'))
        #plt.show()
        #print("")

    if opcion == "5":
        print("\n______________________________________________________________")
        print("\nA = " + str(conjuntoA))
        print("B = " + str(conjuntoB))
        print("C = " + str(conjuntoC))

        conjuntoResultado = []
        cadenaOperaciones = ""

        primerConjunto = input("\nIngrese el primer conjunto con el que empezar A, B o C: ")

        if primerConjunto == "A":
            conjuntoResultado = conjuntoA.copy()
            cadenaOperaciones += "A"

        elif primerConjunto == "B":
            conjuntoResultado = conjuntoB.copy()
            cadenaOperaciones += "B"

        elif primerConjunto == "C":
            conjuntoResultado = conjuntoC.copy()
            cadenaOperaciones += "C"

        while True:
            op = input("Ingrese una operación 1. union. 2. interseccion. 3. diferencia. 4. complemento 5. Volver al menú. ")
            if op == "4":#Complemento
                complemento = []
                for elemento in conjuntoUniversal:
                    if elemento not in conjuntoResultado:
                        complemento.append(elemento)
                conjuntoResultado = complemento.copy()
                cadenaOperaciones = cadenaOperaciones + "'"
                print("\nU = " + str(conjuntoUniversal))

            elif op == "5":#Volver al menú
                    print("______________________________________________________________\n\n")
                    break
            else:
                segundoConjunto = []
                while len(segundoConjunto) == 0:
                    conjunto2Elegido = input("Ingrese un conjunto con el que operar A, B o C: ")
                    segundoConjunto = DiccionarioConjuntos.get(conjunto2Elegido, [])
                    
                if op == "1":#Unión
                    for elemento in segundoConjunto:
                        if elemento not in conjuntoResultado:
                            conjuntoResultado.append(elemento)
                    cadenaOperaciones = "(" + cadenaOperaciones + "U" + conjunto2Elegido + ")"

                elif op == "2":#Intersección
                    interseccion = []
                    for elemento in segundoConjunto:
                        if elemento in conjuntoResultado:
                            interseccion.append(elemento)
                    conjuntoResultado = interseccion.copy()
                    cadenaOperaciones = "(" + cadenaOperaciones + "∩" + conjunto2Elegido + ")"

                elif op == "3":#Diferencia
                    for elemento in segundoConjunto:
                        if elemento in conjuntoResultado:
                            conjuntoResultado.remove(elemento)
                    cadenaOperaciones = "(" + cadenaOperaciones + "-" + conjunto2Elegido + ")"
            
            print("\n" + cadenaOperaciones + " = " + str(conjuntoResultado) + "\n")

    elif opcion == "6":
        break

    if opcion != "5" and opcion != "0":
        resultado = DiccionarioOperaciones.get(opcion, "\n¡¡¡¡¡¡Esa opción no existe!!!!!!\n")
        print("\nA = " + str(conjuntoA))
        print("B = " + str(conjuntoB))
        print("C = " + str(conjuntoC))
        print("\n", resultado, "\n")



    













































