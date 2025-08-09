def mostrar_opciones():
    print('1- SUMA')
    print('2- RESTA')
    print('3- MULTIPLICACION')
    print('4- DIVISION')
    print('5- SALIR')
#----------------------------------------------------------------------------------------------------------------------#
def calculadora():
    mostrar_opciones()
    eleccion = int(input("Ingrese la operación que desea calcular: "))

    while eleccion != 5:
        nro1 = float(input("Ingrese el primer número: "))
        nro2 = float(input("Ingrese el segundo número: "))

        if eleccion == 1:
            print(f"La suma de {nro1} y {nro2} es {nro1 + nro2}")
    #------------------------------------------------------------------------------#
        elif eleccion == 2:
            print(f"La resta de {nro1} y {nro2} es {nro1 - nro2}")
    #------------------------------------------------------------------------------#
        elif eleccion == 3:
            print(f"La multiplicación de {nro1} y {nro2} es {nro1 * nro2}")
    #------------------------------------------------------------------------------#
        elif eleccion == 4:
            if nro2 != 0:
                print(f"La división de {nro1} entre {nro2} es {nro1 / nro2}")
            #----------------------------------------------------------------------#
            else:
                print("Error: no se puede dividir entre cero.")
             #---------------------------------------------------------------------#
    #------------------------------------------------------------------------------#
        else:
            print("Opción no válida.")
        #--------------------------------------------------------------------------#
        mostrar_opciones()
        eleccion = int(input("Ingrese la operación que desea calcular: "))
   #-------------------------------------------------------------------------------#
    print("Saliendo...")
#----------------------------------------------------------------------------------------------------------------------#
