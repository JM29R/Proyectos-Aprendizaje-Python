from ClientesSQL_CLASS import *

opcion = None
while opcion != 5:
    print('''
    1- Listar clientes
    2- Agregar cliente
    3- Editar cliente
    4- Eliminar cliente
    5- Salir
    ''')
    opcion = int(input('ingresar opcion '))
    if opcion == 1:
        clientes = Cliente_DATA.seleccionar()
        print('\nLISTADO DE CLIENTES')
        for cliente in clientes:
            print(cliente)
            print()
        #----------------------------------------------------------------------------------#
    #-------------------------------------------------------------------------------------------------#
    elif opcion == 2:
        nombre_1 = input('Ingrese el nombre del cliente: ')
        apellido_1 = input('Ingrese el apellido del cliente: ')
        membresia_1 =input('Ingrese el membresia del cliente: ')
        cliente = Cliente(nombre=nombre_1,apellido=apellido_1,membresia=membresia_1)
        cliente_insertados = Cliente_DATA.insertar(cliente)
        print(f'clientes insertados: {cliente_insertados}\n')
    #-------------------------------------------------------------------------------------------------#
    elif opcion == 3:
        id_editar = int(input('Ingrese el id del cliente a modificar : '))
        nombre_editar = input('Ingrese el nombre del cliente a modificar : ')
        apellido_editar = input('Ingrese el apellido del cliente a modificar : ')
        membresia_editar = input('Ingrese el membresia del cliente a modificar : ')
        cliente_editar =Cliente(id_editar,nombre_editar,apellido_editar,membresia_editar)
        clientes_editados = Cliente_DATA.actualizar(cliente_editar)
        print(f'clientes editados: {clientes_editados}\n')
    #-------------------------------------------------------------------------------------------------#
    elif opcion == 4:
        id_eliminar = int(input('Ingrese el ID del cliente a eliminar: '))
        cliente = Cliente(id_eliminar)
        eliminados = Cliente_DATA.eliminar(cliente)
        print(f'clientes eliminados: {eliminados}\n')
    #-------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
else:
        print('Saliendo.............')
#----------------------------------------------------------------------------------------------------------------------#