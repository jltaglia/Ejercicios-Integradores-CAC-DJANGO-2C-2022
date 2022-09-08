def get_int_iter(cadena):
    '''
    Lee un valor entero ingresado por el usuario y lo devuelve,
    iterando mientras el valor no sea correcto.
    (**) RESUELTO EN FORMA ITERATIVA
    '''
    try:
        numero = int(cadena)
        return numero
    except ValueError:
        return False

def get_int_recurs(cadena):
    '''
    Lee un valor entero ingresado por el usuario y lo devuelve,
    iterando mientras el valor no sea correcto.
    (**) RESUELTO EN FORMA RECURSIVA
    '''
    cadena = input('ingrese la cadena a convertir: ')
    try:
        numero = int(cadena)
        print('Cadena convertida =', numero)
        return
    except ValueError:
        print('La cadena no se puede convertir')

    get_int_recurs(cadena)

if __name__ == '__main__':
    print('-' * 30)
    print('En forma iterativa...')
    print('-' * 30)
    while True:
        resultado = get_int_iter(input('Ingrese la cadena a convertir en número: '))
        if not resultado:
            print('La cadena no se puede convertir en número...')
        else:
            print('Cadena convertida =', resultado)
            break


    print('-' * 30)
    print('En forma recursiva...')
    print('-' * 30)
    get_int_recurs('')
