from ejercicio_7 import Cuenta


class CuentaJoven(Cuenta):
    __slots__ = ('__titular','__cantidad','__bonific','__edad')

    def __init__(self, titular, bonific, **kwargs):
        super().__init__(titular = '', **kwargs)
        self.titular = titular
        self.bonific = bonific
        self.edad = 0
        # LA PROPIEDAD 'edad' SI BIEN NO FIGURA EN LA ESPECIFICACION
        # DEL EJERCICIO, CREO ES NECESARIA PARA PODER UTILIZAR EL 
        # METODO REQUERIDO 'es_titular_valido'

    @property
    def bonific(self):
        return self.__bonific

    @bonific.setter
    def bonific(self, bonific: float = 0.0):
        self.__bonific = bonific

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad: int = 0):
        self.__edad = edad

    def retirar(self, cant):
        if self.es_titular_valido():
            super().retirar(cant)
        else:
            print('El titular no puede realizar retiros...')

    def es_titular_valido(self):
        if self.edad > 18 and self.edad < 25:
            return True
        else:
            return False

    def mostrar(self):
        msg = super().mostrar()
        msg += f'\nCUENTA JOVEN\n'
        msg += f'Bonificación: {self.bonific:4.1f}%'
        return msg


if __name__ == '__main__':

    cj1 = CuentaJoven('Julian', 10)
    print('Después de instanciar el objeto CuentaJoven()')
    print(cj1.mostrar(),'\n')

    cj1.ingresar(10000)
    print('Después de ingresar(10000)')
    print(cj1.mostrar(),'\n')

    cj1.retirar(500)
    print('Después de retirar(500)')
    print(cj1.mostrar(),'\n')

    cj2 = CuentaJoven('Paula', 15, 20)
    print('Después de instanciar el objeto CuentaJoven()')
    print(cj1.mostrar(),'\n')

    cj1.ingresar(5000)
    print('Después de ingresar(5000)')
    print(cj1.mostrar(),'\n')

    cj1.retirar(4000)
    print('Después de retirar(4000)')
    print(cj1.mostrar(),'\n')