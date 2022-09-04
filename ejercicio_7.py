class Cuenta:
    def __init__(self, titular, *kargs):
        self.__titular = titular
        self.__cantidad = 0.0

    @property
    def titular(self):
        return self.__titular

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @property
    def cantidad(self):
        return self.__cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad += cantidad

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad(cantidad)

    def retirar(self, cantidad):
        self.cantidad(cantidad * -1)

    def mostrar(self):
        return f'Datos de la Cuenta:\nTitular: {self.__titular}\n  Saldo: {self.__cantidad}'


if __name__ == '__main__':
    c1 = Cuenta('Julian')

    print(c1.mostrar())
    
    c1.ingresar(10000)
    print(c1.mostrar())
    