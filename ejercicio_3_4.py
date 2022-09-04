def dev_dic(cadena):
    palabras = [palabra for palabra in cadena.split()]
    cantidades = [palabras.count(palabra) for palabra in palabras]
    diccionario = {palabra:cantidad for (palabra,cantidad) in zip(palabras,cantidades)}

    return diccionario

def mas_apariciones(diccionario):
    mas_veces = max(diccionario.items(), key=lambda item: item[1])
    return mas_veces


if __name__ == '__main__':
    contadas = dev_dic('Al saber esto, la PFA envió un patrullero a la casa en Condarco, donde los efectivos se encontraron con un hermano de Herrera, que les relató de su fallecimiento. Archivos consultados por Infobae revelan que Herrera estaba registrado en el rubro de taxis de la AFIP, el mismo en el que estaba registrado Sabag Montiel, y que había sido empleado de una conocida empresa de transporte de caudales.')
    print(contadas)

    mas_repetida = mas_apariciones(contadas)
    print(f'\nLa palabra que mas se repite es "{mas_repetida[0]}", porque se repite {mas_repetida[1]} veces')