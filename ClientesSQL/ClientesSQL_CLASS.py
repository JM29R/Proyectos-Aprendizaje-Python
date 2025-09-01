from ClientesSQL_conexion import *


class Cliente:
    def __init__(self, id=None, nombre=None, apellido=None, membresia=None):
        self.ID = id
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    #----------------------------------------------------------------------------------------#
    def __str__(self):
        return (f'Id: {self.ID}, Nombre {self.nombre}, '
                f'Apellido: {self.apellido}, Membresia: {self.membresia}')
    #----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class Cliente_DATA:
    SELECCIONAR = 'SELECT * FROM cliente'
    INSERTAR = 'INSERT INTO cliente (nombre, apellido, membresia) VALUES (%s, %s, %s)'
    ACTUALIZAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            #-------------------------------------------------------------------------#
            return clientes
        #----------------------------------------------------------------------------------#
        except Error as e:
            print(f'Ocurrio un error al seleccionar clientes: {e}')
            return []
        #----------------------------------------------------------------------------------#
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
            #-------------------------------------------------------------------------#
        #----------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------#
    @classmethod
    def insertar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores= (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount
        #----------------------------------------------------------------------------------#
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
            return 0
        #----------------------------------------------------------------------------------#
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
        #----------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------#
    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia, cliente.ID)
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount
        #----------------------------------------------------------------------------------#
        except Exception as e:
            print(f'Ocurrio un error al actualizar cliente: {e}')
        #----------------------------------------------------------------------------------#
        finally:
            if cursor is not None:
                cursor.close()
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
        #----------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------#
    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        cursor = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (cliente.ID,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount
        #----------------------------------------------------------------------------------#
        except Exception as e:
            print(f'Ocurrio un error al eliminar cliente: {e}')
        #----------------------------------------------------------------------------------#
        finally:
            if cursor is not None:
                cursor.close
            if conexion is not None:
                Conexion.liberar_conexion(conexion)
        #----------------------------------------------------------------------------------#
    #-----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
# if __name__ == '__main__':
    #Insertar
    # cliente1 = Cliente(nombre='Juan', apellido='Rios',membresia=300)
    # clientes_insertados = Cliente_DATA.insertar(cliente1)
    # print(clientes_insertados)

    #seleccionar clientes
    # clientes = Cliente_DATA.seleccionar()
    # for cliente in clientes:
    #     print(cliente)

    #actualizar
    # cliente_actualizar = Cliente(3, 'Juan Manuel','Rios',400)
    # clientesActualizados = Cliente_DATA.actualizar(cliente_actualizar)
    # print(clientesActualizados)

    #Eliminar Clientes
    # cliente_eliminar = Cliente(id=4)
    # clientes_eliminados= Cliente_DATA.eliminar(cliente_eliminar)
    # print(clientes_eliminados)
