from Catalogo_Peliculas import *
print('---Catalogo de Peliculas---')
opcion = None
while opcion != 4:
    try:
        print('''Opciones:
        1- Agregar Listas
        2- Listar Peliculas
        3- Eliminar Catalogo
        4- Salir ''')
        opcion = int(input('ingresar opcion'))
        if opcion == 1:
            nombre_pelicula = input('ingresar un nombre de pelicula')
            pelicula = Pelicula(nombre_pelicula)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        #--------------------------------------------------------------------------------------#
        elif opcion == 2:
            CatalogoPeliculas.listar_peliculas()
        #--------------------------------------------------------------------------------------#
        elif opcion == 3:
            CatalogoPeliculas.eliminar_peliculas()
        #--------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
    except Exception as e:
        print(f'Ocurrio un error: {e}')
        opcion = None
#----------------------------------------------------------------------------------------------------------------------#
