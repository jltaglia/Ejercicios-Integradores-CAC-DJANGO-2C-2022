from ejercicio_1 import mcd

def mcm(x,y):
    '''
    Calcula el mínimo común múltiplo entre dos números x, y
    utilizando el máximo común divisor de ellos y la siguiente
    formula:
        mcm(x,y) = (x * y) / mcd(x,y)
    '''
    mcd_ab = mcd(x,y)[1]
    min_com_mul = int((x * y) / mcd_ab)
    return f'mcm ({x},{y}) = {min_com_mul}'


if __name__ == '__main__':
    print(mcm(72,50))
