def mcd(x,y):
    '''
    Calcula el máximo común divisor entre dos números x, y
    utilizando el Algoritmo de Euclides:
        Si y = 0 => mcd(x,y) = x
        Si no mcd(x,y) = mcd(y, x % y)
    '''
    if y == 0:
        return f'MCD ({x},{y}) = {a}', a
    else:
        a = x
        b = y
        resto = 1
        while resto != 0:
            resto = a % b
            a = b
            b = resto

        return f'MCD ({x},{y}) = {a}', a

if __name__ == '__main__':
    print(mcd(2366,273)[0])
    print(mcd(48,60)[0])