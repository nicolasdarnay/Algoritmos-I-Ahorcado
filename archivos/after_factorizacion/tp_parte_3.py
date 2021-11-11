from random import choice

import tp_parte_2

DICCIONARIO_DE_PALABRAS = tp_parte_2.obtener_diccionario()


def diccionario_reducido(diccionario, longitud):
    """Genera un nuevo diccionario basado en el introducido,
     con palabras de igual longitud a la solicitada
     Autor: Nicolás Darnay"""

    rv = {}
    for palabra in diccionario:
        if len(palabra) == longitud:
            rv.update({palabra:diccionario[palabra]})
    return rv


def palabra_aleatoria(diccionario, largo_palabra=0):
    """Obtiene una palabra aleatoria del diccionario de largo_palabra
    longitud. Autor: Nicolás Darnay"""

    if largo_palabra == 0:
        rv = choice(list(diccionario.keys()))
    else:
        rv = choice(list(diccionario_reducido(diccionario, largo_palabra).keys()))
    return rv