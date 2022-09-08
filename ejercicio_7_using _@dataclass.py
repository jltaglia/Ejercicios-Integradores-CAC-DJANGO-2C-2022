from dataclasses import dataclass

@dataclass
class Cuenta:
    titular: str
    cantidad: float = 0.0

    __slots__ = ['__titular','__cantidad']

    def __init__(self, titular: str):
        self.titular = titular
        self.cantidad = 0.0

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
    def cantidad(self, cantidad: float = 0.0):
        self.__cantidad = cantidad

    def ingresar(self, cant):
        if cant > 0:
            cant_ant = self.cantidad
            self.cantidad = (cant_ant + cant)

    def retirar(self, cant):
        if cant < 0:
            # POR LAS DUDAS QUE EL USUARIO HAYA INGRESADO
            # POR ERROR UNA CANTIDAD NEGATIVA PARA RETIRAR 
            cant = cant * -1
        cant_ant = self.cantidad
        self.cantidad = cant_ant - cant

    def mostrar(self):
        return f'Datos de la Cuenta:\nTitular: {self.titular}\n  Saldo: {self.cantidad}'


if __name__ == '__main__':
    c1 = Cuenta('Julian')
    print('Después de instanciar el objeto Cuenta()')
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
        print('(*) Este error aparece, gracias al uso de __slots__,\nal querer asignar al objeto una propiedad inexistente.\n')
