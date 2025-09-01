class Orden:
    contador_ordenes = 0
    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self.id_orden = Orden.contador_ordenes
        self.computadoras = computadoras
    #----------------------------------------------------------------------------------------------#
    def __str__(self):
        computadoras_str= ' '
        for computadora in self.computadoras:
            computadoras_str +='\n'+ computadora.__str__()
        return f'''Orden #{self.id_orden} 
        Computadoras: {computadoras_str}'''
        #-------------------------------------------------------------------------------------#
    #----------------------------------------------------------------------------------------------#
    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)
    #----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class Computadora:
    contador_computadora = 0
    def __init__(self,nombre, monitor,
                 teclado, raton ):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.raton = raton
        self.teclado = teclado
    #----------------------------------------------------------------------------------------------#
    def __str__(self):
        return f'''COMPUTADORA {self.nombre} : {self.id_computadora}
        MONITOR: {self.monitor}
        RATON: {self.raton}
        TECLADO: {self.teclado}'''
    # ----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class Monitores:
    contador_monitores = 0
    def __init__(self, Marca, Tamanio):
        Monitores.contador_monitores += 1
        self.id_monitores = Monitores.contador_monitores
        self.Marca = Marca
        self.Tamanio = Tamanio
    #----------------------------------------------------------------------------------------------#
    def __str__(self):
        return f'MONITOR ID:{self.id_monitores}, MARCA:{self.Marca}, TAMAÑO:{self.Tamanio}'
    #----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self.marca = marca
        self.tipo_entrada = tipo_entrada
    #----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclados += 1
        self.id_teclado = Teclado.contador_teclados
        super().__init__(marca, tipo_entrada)
    #----------------------------------------------------------------------------------------------#
    def __str__(self):
        return f'TECLADO ID: {self.id_teclado}, MARCA: {self.marca}, TIPO DE ENTRADA: {self.tipo_entrada}'
#----------------------------------------------------------------------------------------------------------------------#
class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self.id_raton =Raton.contador_ratones
        super().__init__(marca, tipo_entrada)
    #----------------------------------------------------------------------------------------------#
    def __str__(self):
        return f'MOUSE ID: {self.id_raton}, MARCA: {self.marca}, TIPO DE ENTRADA: {self.tipo_entrada}'
    #----------------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------------------------------------#
