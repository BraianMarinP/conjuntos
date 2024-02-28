import matplotlib.pyplot as plt
from matplotlib_venn import venn3



class OperadorConjunto:
    def Union(self, conjA, conjB, conjC):
        conjuntoUnion = []
        for elemento in conjA:
            conjuntoUnion.append(elemento)

        for elemento in conjB:
            if elemento not in conjuntoUnion:
                conjuntoUnion.append(elemento)

        for elemento in conjC:
            if elemento not in conjuntoUnion:
                conjuntoUnion.append(elemento)
        
        return "AvBvC = " + str(conjuntoUnion)
    
    def Interseccion(self, conjA, conjB, conjC):
        conjInterseccion = []
        for elemento in conjA:
            if elemento in conjB and elemento in conjC:
                conjInterseccion.append(elemento)
        
        return "AnBnC = " + str(conjInterseccion)

    def Diferencia(self, conjA, conjB, conjC):
        conjDiferencia = []
        for elemento in conjA:
            conjDiferencia.append(elemento)
        for elemento in conjB:
            if elemento in conjDiferencia:
                conjDiferencia.remove(elemento)
        for elemento in conjC:
            if elemento in conjDiferencia:
                conjDiferencia.remove(elemento)    
        
        return "A-B-C = " + str(conjDiferencia)

    def Complemento(self, conjA, conjB, conjC, conjUniversal):
        complementoA = []
        complementoB = []
        complementoC = []

        for elemento in conjUniversal:
            if elemento not in conjA:
                complementoA.append(elemento)
            if elemento not in conjB:
                complementoB.append(elemento)
            if elemento not in conjC:
                complementoC.append(elemento)
        
        return "\nU = " + str(conjUniversal) +  " \nA' = " + str(complementoA) + "\nB' = " + str(complementoB) + "\nC' = " + str(complementoC)



operador = OperadorConjunto()


cadenaA = input("Ingrese un conjunto A separando elementos por comas: ")
cadenaB = input("Ingrese un conjunto B separando elementos por comas: ")
cadenaC = input("Ingrese un conjunto C separando elementos por comas: ")

conjuntoA = cadenaA.split(",")
conjuntoB = cadenaB.split(",")
conjuntoC = cadenaC.split(",")
conjuntoUniversal = []

def generar_diagrama3():
    set1 = set(conjuntoA)
    set2 = set(conjuntoB)
    set3 = set(conjuntoC)

    # Calcular las intersecciones
    intersecciones = {
        '100': set1 - set2 - set3,
        '010': set2 - set1 - set3,
        '001': set3 - set1 - set2,
        '110': set1 & set2 - set3,
        '101': set1 & set3 - set2,
        '011': set2 & set3 - set1,
        '111': set1 & set2 & set3
    }

    # Crear el diagrama de Venn
    venn = venn3(subsets=(len(set1 - set2 - set3), len(set2 - set1 - set3), len(set1 & set2 - set3),
                          len(set3 - set1 - set2), len(set1 & set3 - set2), len(set2 & set3 - set1),
                          len(set1 & set2 & set3)),
                 set_labels=('A', 'B', 'C'))

    # Mostrar los elementos de cada conjunto sin comas
    for subset, conjunto in intersecciones.items():
        if venn.get_label_by_id(subset) is not None:
            venn.get_label_by_id(subset).set_text(
                '\n'.join(sorted(conjunto)))  # Usamos '\n' para separar los elementos en líneas

    # Ajustar el espaciado de las etiquetas
    for text in venn.set_labels:
        text.set_fontsize(11)  # Tamaño de fuente
        text.set_fontweight('bold')  # Negrita
        text.set_color('black')  # Color del texto

    plt.show()





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



    













































