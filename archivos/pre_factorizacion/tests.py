#lo separo en otro archivo para hacerlo más extensible
#acá podrían agregar tests hechos a todas las fases también
import random as r

import tp_parte_2 as dos

import tp_parte_3 as tres


def test_fase_2():
    diccionario = dos.obtener_diccionario()
    """tests con el texto provisto en la fase 2"""
    # "mucho" aparece 26 veces, una como ¡mucho!
    assert diccionario["mucho"] == 26
    # "cristo" aparece 5 veces entre exclamaciones
    assert diccionario["cristo"] == 5
    # "gafarro" aparece una vez como "Gafarró"
    assert diccionario["gafarro"] == 2
    # "era" es demasiado corta para estar en el diccionario
    assert "era" not in diccionario
    # "paella" aparece 3 veces como _paella_ y una vez como paella
    assert diccionario["paella"] == 4
    for palabra in diccionario.keys():
        for caracter in palabra:
            assert caracter.isalpha()


def test_fase_3():
    """Forma una lista con 100 numeros entre la minima y maxima longitud
    de palabras en el texto y prueba"""
    diccionario = dos.obtener_diccionario()
    #no hay palabras más largas que esto
    maxima_longitud = 16
    #longitud minima del texto
    minima_longitud = 5
    numeros = [r.randint(minima_longitud, maxima_longitud) for x in range(0,100)]
    for numero in numeros:
        palabra = tres.palabra_aleatoria(diccionario,numero)
        assert len(palabra) == numero