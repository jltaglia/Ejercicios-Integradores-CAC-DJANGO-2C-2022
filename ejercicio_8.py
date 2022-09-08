from ejercicio_7 import Cuenta


class CuentaJoven(Cuenta):
    '''
    CuentaJoven:
    - La Cuenta Joven debe ser iniciada con el nombre del titular
      y por ser una Cuenta Joven debe incluir el porcentaje de 
      bonificaión asignado.
    - La cantidad se debe ingresar a través del método
      correspondiente ingresar() y modificar a través 
      del método retirar() solo si el titular es válido
      (mayor de edad y menor de 25 años).
    - Para ver los datos de la cuenta usar el método
      mostrar().
    '''

    __slots__ = ('__titular','__cantidad','__bonific','__edad')

    def __init__(self, titular, bonific, edad = 0, **kwargs):
        super().__init__(titular = '')
        self.titular = titular
        self.bonific = bonific
        self.edad = edad
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
        if self.es_titular_valido():
            msg += f'    ** CUENTA JOVEN **\n'
            msg += f'    Bonificación: {self.bonific:4.1f}%'
        return msg


if __name__ == '__main__':

    print(CuentaJoven.__doc__)

    cj1 = CuentaJoven('Julian', 10)
    print('Creando la Cuenta Joven de Julian con 10% de bonificación')
    print(cj1.mostrar(),'\n')

    print('Ingreso 10000 a la Cuenta Joven de Julian')
    cj1.ingresar(10000)
    print('Después de ingresar(10000)')
    print(cj1.mostrar(),'\n')

    print('Voy a retirar 500 de la cuenta de Julian')
    cj1.retirar(500)
    print('...lo cual no va a ser posible porque Julian no tiene edad ingresada')
    print(cj1.mostrar(),'\n')

    cj2 = CuentaJoven('Paula', 15, 20)
    print('Creando la Cuenta Joven de Paula con 15% de bonificaión y 20 años')
    print(cj2.mostrar(),'\n')

    print('Ingreso 5000 a la Cuenta Joven de Paula')
    cj2.ingresar(5000)
    print(cj2.mostrar(),'\n')

    print('Retiro 4500 de la Cuenta Joven de Paula')
    cj2.retirar(4500)
    print(cj2.mostrar(),'\n')
