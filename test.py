dni = 23645093
if len(dni) > 8 or not dni.isnumeric():
    # EL DNI TIENE COMO MAX 8 NUMEROS
    while True:
        print(f'EL DNI no tiene el formato adecuado...')
        dni = input('Ingrese un DNI como máximo 8 numeros: ')
        break