class Cuenta:
    '''
    Cuenta:
    - La Cuenta debe ser iniciada con el nombre del titular.
    - La cantidad solo se debe ingresar a través del método
      correspondiente ingresar() y modificar solo a través 
      del método ingresar() o retirar().
    - Para ver los datos de la cuenta usar el método
      mostrar().
    '''

    __slots__ = ('__titular','__cantidad')
    
    def __init__(self, titular):
        self.__titular = titular
        self.__cantidad = 0.0

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular: str = ''):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    def ingresar(self, cant):
        if cant > 0:
            self.cantidad += cant
            # cantidad(cantidad)

    def retirar(self, cant):
        if cant < 0:
            # POR LAS DUDAS QUE EL USUARIO HAYA INGRESADO
            # UNA CANTIDAD NEGATIVA
            cant = cant * -1
        self.cantidad -= cant

    def mostrar(self):
        msg = f'    Datos de la Cuenta:\n'
        msg += f'    Titular: {self.titular}\n'
        msg += f'      Saldo: {self.cantidad:12.2f}\n'
        return msg


if __name__ == '__main__':
    c1 = Cuenta('Julian')
    print('Creando la Cuenta de Julian')
    print(c1.mostrar(),'\n')

    c1.ingresar(10000)
    print('Después de ingresar(10000)')
    print(c1.mostrar(),'\n')

    c1.retirar(500)
    print('Después de retirar(500)')
    print(c1.mostrar(),'\n')

    try:
        c1.deuda = -5000
    except AttributeError:
        print("AttributeError: 'Cuenta' object has no attribute 'deuda'")
        print('(*) Este error aparece, gracias al uso de __slots__,')
        print('al querer asignar al objeto una propiedad inexistente.')