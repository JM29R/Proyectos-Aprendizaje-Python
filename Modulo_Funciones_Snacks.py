def mostrar_menu():
    print('1-Comprar Snack')
    print('2-Mostrar Ticket')
    print('3-Salir')
#---------------------------------------------------------------------------------------------------------------------#
def mostrar_listado():
    print('0-Papas $30')
    print('1-Refresco $50')
    print('2-sandwich $120')
#---------------------------------------------------------------------------------------------------------------------#
def maquina_snacks(snacks,productos):
    salir = False
    while not salir:
        mostrar_menu()
        opcion=int( input('selecciona una opcion!'))
        if opcion==1:
            comprar_producto(snacks,productos)
        elif   opcion == 2:
            mostrar_ticket(productos)
        elif opcion == 3:
            print('regresa pronto')
            salir = True
        else:
            print('opcion invalida selecciona otra opcion')

#---------------------------------------------------------------------------------------------------------------------#
def comprar_producto(snacks,productos):
    mostrar_listado()
    id_snack =int( input('que snack quieres?'))
    productos.append(snacks[id_snack])

#---------------------------------------------------------------------------------------------------------------------#
def mostrar_ticket(productos):
    ticket = f'\t*** Ticket de Venta***'
    total=0
    for producto in productos:
        ticket += f"\n\t {producto['nombre']} - {producto['precio']} -"
        total += producto['precio']
    ticket += f'\n\tTOTAL ->${total}'
    print(ticket)
#---------------------------------------------------------------------------------------------------------------------#