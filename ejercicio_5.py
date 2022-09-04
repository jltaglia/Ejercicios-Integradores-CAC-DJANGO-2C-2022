def get_int(cadena):
    if cadena == 'salir':
        print('Listo...')
        return None
    cadena = input('ingrese la cadena a convertir:')
    try:
        numero = int(cadena)
        print(numero)
    except:
        print('La cadena no se puede convertir')

    get_int(cadena)

if __name__ == '__main__':
    get_int('')
