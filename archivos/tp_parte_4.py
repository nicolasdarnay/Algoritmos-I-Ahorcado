import tp_parte_2

import tp_parte_3


LONGITUD_MINIMA = tp_parte_2.LONGITUD_MINIMA

def sacar_longitud_maxima(diccionario):
    """Consigue la longitud máxima de palabra en el diccionario
    Autores: Roy Fiorilo/Ignacio Chacón"""
    
    lista_de_longitudes = [len(llave) for llave in diccionario.keys()]
    return max(lista_de_longitudes)


def solicitud_de_ingreso():
    """Pregunta al usuario si quiere ingresar una longitud específica
    antes de jugar
    Autores: Roy Fiorilo/Ignacio Chacón"""
    
    rv = input("¿Quiere ingresar una longitud para la palabra? si/no: ")
    
    while rv not in ("si","no"):
        rv = input("Por favor, responda con si/no: ")
    
    return rv == "si"


def ingreso():
    """solicita el ingreso de una longitud al usuario
    Autores: Roy Fiorilo/Ignacio Chacón"""
    rv = 0
    while rv <= 0:
        try:
            rv = int(input("Ingrese la longitud deseada: "))
            if rv < 0:
                print("Ingrese un numero MAYOR a 0")
        except:
            print("Por favor, ingrese un NUMERO NATURAL")
    return rv


def palabra_con_longitud(diccionario, longitud):
    """ devuelve una palabra con la longitud deseada
    Autor Ignacio Orona
    """
    return tp_parte_3.palabra_aleatoria(diccionario, longitud)

def palabra(diccionario):
    """consigue una palabra del diccionario tras pedirle ingreso  al jugador
    Autores: Roy Fiorilo/Ignacio Chacón"""
    
    if solicitud_de_ingreso():
        longitud = validar_ingreso(ingreso(), diccionario)
        rv = tp_parte_3.palabra_aleatoria(diccionario, longitud)
    else:
        rv = tp_parte_3.palabra_aleatoria(diccionario)
    return rv


def validar_ingreso(longitud, diccionario):
    """ Valida el ingreso de la longitud de ingreso()
    Autores: Roy Fiorilo/Ignacio Chacón"""
    longitud_maxima = sacar_longitud_maxima(diccionario)
    rv = longitud
    while rv <= LONGITUD_MINIMA or rv > longitud_maxima:
        print("No existe palabra con esa longitud en el texto")
        rv = ingreso()
    return rv