from pprint import pprint

def dev_dic(cadena):
    '''
    Recibe una cadena de caracteres y devuelve un diccionario con cada palabra
    que contiene y la cantidad de veces que aparece cada una (frecuencia).
    '''
    palabras = [palabra for palabra in cadena.split()]
    cantidades = [palabras.count(palabra) for palabra in palabras]
    diccionario = {palabra:cantidad for (palabra,cantidad) in zip(palabras,cantidades)}

    return diccionario

def mas_apariciones(diccionario):
    '''
    Recibe un diccionario y devuelve una tupla con la 
    palabra más repetida dentro de la cadena y su frecuencia.
    '''
    mas_veces = max(diccionario.items(), key=lambda item: item[1])
    return mas_veces


if __name__ == '__main__':
    dicio = '''El único lugar normal es el vacío vasto, frío y universal,
     la noche perpetua del espacio intergaláctico, un lugar tan extraño y desolado que 
     en comparación suya los planetas, las estrellas y las galaxias se nos antojan algo
     dolorosamente raros y preciosos. Si nos soltaran al azar dentro del Cosmos la 
     probabilidad de que nos encontráramos sobre un planeta o cerca de él sería inferior
     a una parte entre mil millones de billones de billones ( 10^33 , un uno seguido de 
     33 ceros ). En la vida diaria una probabilidad así se considera nula. Los mundos 
     son algo precioso. CARL SAGAN - COSMOS'''
    
    dicio_contadas = dev_dic(dicio)
    print(dicio_contadas)

    mas_repetida = mas_apariciones(dicio_contadas)
    print(f'\nLa palabra que mas se repite es "{mas_repetida[0]}", porque se repite {mas_repetida[1]} veces')