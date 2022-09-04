class Persona:
    def __init__(self):
        self.__nombre = ''
        self.__edad = 0
        self.__dni = ''

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        # SI LA PERSONA POR ERROR ES MUY JOVEN O MUY VIEJA 
        while edad <= 0 or edad > 120:
            print(f'{edad} años de edad? ...no está bién.')
            edad = int(input('Cual sería la edad correcta?: '))

        self.__edad = edad

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        # EL DNI TIENE COMO MAX 8 NUMEROS
        while len(dni) > 8 or not dni.isnumeric():
            print(f'EL DNI no tiene el formato adecuado...')
            dni = input('Ingrese un DNI como máximo 8 numeros: ')

        self.__dni = dni

    def mostrar(self):
        return f'Nombre: {self.__nombre}\n  Edad: {self.__edad}\n   DNI: {self.__dni}'

    def es_mayor_de_edad(self):
        return int(self.edad) >= 18


if __name__ == '__main__':
    
    # INTENO DE ACCESO A LAS PROPIEDADES DEL OBJETO PERSONA
    # EN FORMA DIRECTA
    try:
        print("p1 = Persona('Julian', 48, '12345678')")
        p1 = Persona('Julian', 48, '12345678')
    except TypeError:
        print('ERROR: no se puede asignar de esta forma los datos de la persona')
    try:
        print(p1.mostrar())
        print('Es mayor de edad?:', p1.es_mayor_de_edad())
    except NameError:
        print('ERROR: como no pude asignar directamente los datos\n       la persona no existe (el objeto no se instanció)\n')

    try:
        print("p2 = Persona('Paula', 15, '87654321')")
        p2 = Persona('Paula', 15, '87654321')
    except TypeError:
        print('ERROR: no se puede asignar de esta forma los datos de la persona')
    try:
        print(p2.mostrar())
        print('Es mayor de edad?:', p2.es_mayor_de_edad())
    except NameError:
        print('ERROR: como no pude asignar directamente los datos\n       la persona no existe (el objeto no se instanció)\n')


    print('-' * 30)
    print('Acceso através de los setters')
    print('-' * 30)
    p1 = Persona()
    p1.nombre = 'Julian'
    p1.edad = 48
    p1.dni = '12345678'
    
    p2 = Persona()
    p2.nombre = 'Paula'
    p2.edad = 15
    p2.dni = '87654321'
    
    print(p1.mostrar())
    print('Es mayor de edad?:', p1.es_mayor_de_edad(),'\n')
    print(p2.mostrar())
    print('Es mayor de edad?:', p2.es_mayor_de_edad(),'\n')