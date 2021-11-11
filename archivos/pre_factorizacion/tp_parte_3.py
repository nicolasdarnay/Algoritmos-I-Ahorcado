import random

import tp_parte_2

diccionario_de_palabras = tp_parte_2.obtener_diccionario()


def diccionario_reducido(diccionario, longitud):
    """Genera un nuevo diccionario basado en el introducido,
     con palabras de igual longitud a la solicitada
     Autor: Nicolás Darnay"""

    diccionario_nuevo = {}
    for palabra in diccionario:
        if len(palabra) == longitud:
            diccionario_nuevo.update({palabra:diccionario[palabra]})
    return diccionario_nuevo

def obtener_palabra(diccionario):
    """Obtiene una palabra aleatoria
    Autor: Nicolás Darnay"""

    diccionario_lista = list(diccionario)
    palabra = random.choice(diccionario_lista)
    return palabra

def palabra_aleatoria(diccionario, largo_palabra=0):
    """Obtiene una palabra de cierta longitud. Si no se ingresa ninguna 
    longitud retorna cualquier palabra de cualquier largo
    Autor: Nicolás Darnay"""

    if largo_palabra == 0:
        rv = obtener_palabra(diccionario)
    else:
        rv = obtener_palabra(diccionario_reducido(diccionario, largo_palabra))
    return rv

#print(palabra_aleatoria(diccionario_de_palabras,16))