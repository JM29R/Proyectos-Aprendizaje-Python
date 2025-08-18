import  os
class Pelicula:
    def __init__(self,nombre):
        self.nombre = nombre
    #-----------------------------------------------------------------------------------------------------------#
    def __str__(self):
        return f'pelicula: {self.nombre}'
    #-----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class CatalogoPeliculas:
    nombre_archivo= 'peliculas.txt'
    @classmethod
    def agregar_pelicula(cls, Pelicula):
        with open(cls.nombre_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{Pelicula.nombre}\n')
    #-----------------------------------------------------------------------------------------------------------#
    @classmethod
    def listar_peliculas(cls):
        with open(cls.nombre_archivo,'r', encoding='utf8') as archivo:
            print('Lista de Peliculas')
            print(archivo.read())
    #-----------------------------------------------------------------------------------------------------------#
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.nombre_archivo)
        print(f'Archivo eliminado: {cls.nombre_archivo}')
    #-----------------------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
