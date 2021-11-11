import random as r
import doctest
import TP1_Estonios as uno
import tp_parte_2 as dos
import tp_parte_3 as tres
import tp_parte_4 as cuatro


#--------------AQUI EMPIEZA LA GRAN MURALLA DE DOCTESTS-----------------------#
#etapa 1
"""
>>> uno.palabra_adivinada(adivinada,["a","d","i","v","n"])
True
>>> uno.palabra_adivinada(adivinada,["a","d","i"])
False
>>> uno.palabra_secreta(adivinada,["a"])
a?????a?a
>>> uno.palabra_secreta(adivinada,[])
?????????
>>> uno.palabra_secreta(adivinada,["a","d","i","v","n"])
adivinada
>>> uno.dame_desaciertos(["a","b"])
2 - ab
>>> uno.dame_desaciertos([])
0 -
>>> uno.ultima_es_0_fin([])
False
>>> uno.ultima_es_0_fin(["q","a","0"])
True
"""

#etapa 2
"""
>>> dos.es_valida("John")
True
>>> dos.es_valida("estrepitosamente")
True
>>> dos.es_valida("J0hn")
False
>>> dos.es_valida("")
False
>>> dos.es_valida("0John")
False
>>> dos.es_valida("Jon")
False
>>> dos.es_valida("ª")
False
>>> dos.eliminar_invalidos_internos(["a","b","c","4","d"])
["a","b","c"," ", "d"]
>>> dos.eliminar_invalidos_internos(["a","b","c","d"])
["a","b","c","d"]
>>> dos.limpiar_palabra(["a","b","c",",","d"])
["abc","d"]
>>> dos.limpiar_palabra(["Buenas_tardes_muchachos"])
["Buenas", "tardes", "muchachos"]
>>> dos.limpiar_palabra(["4564534"])
[""]

>>> dos.limpiar_lista(["Mamá", "Buenas_tardes_muchachos", 
"Buenas_noches_muchachada", "supercalifrastilísticoespialidoso", "ñandú",
"ósóbúcó_al_horno", "Martín_Castillo"])
['mama', 'buenas', 'tardes', 'muchachos', 'noches', 'muchachada',
 'supercalifrastilisticoespialidoso', 'nandu', 'osobuco', 'al',
 'horno', 'martin', 'castillo']
>>> dos.conseguir_palabras_validas("Lorem ipsum dolor sit amet, consectetur 
adipiscing elit. Nunc blandit lobortis nunc, sed dictum nisi iaculis at. 
Suspendisse sed faucibus arcu, id bibendum est. Sed ut gravida nisl. Nunc 
sodales placerat risus a euismod. Aenean a egestas eros, vel maximus quam. 
Maecenas velit ex, tincidunt vel est consectetur, imperdiet auctor ligula. 
In semper placerat justo, at mollis sem molestie at. Pellentesque cursus, 
lacus non egestas rhoncus, diam ipsum semper erat, at molestie libero enim 
a nulla. Suspendisse potenti. Aenean auctor vestibulum dui. Sed non turpis 
magna. Duis rhoncus nec dui ut luctus. Aliquam in elit dictum ipsum hendrerit 
iaculis.")
{'lorem': 1, 'ipsum': 3, 'amet': 1, 'consectetur': 2, 'adipiscing': 1,
 'elit': 2, 'nunc': 3, 'blandit': 1, 'lobortis': 1, 'dictum': 2, 'nisi': 1,
 'iaculis': 2, 'suspendisse': 2, 'faucibus': 1, 'arcu': 1, 'bibendum': 1,
 'gravida': 1, 'nisl': 1, 'sodales': 1, 'placerat': 2, 'risus': 1,
 'euismod': 1, 'aenean': 2, 'egestas': 2, 'eros': 1, 'maximus': 1,
 'quam': 1, 'maecenas': 1, 'velit': 1, 'tincidunt': 1, 'imperdiet': 1,
 'auctor': 2, 'ligula': 1, 'semper': 2, 'justo': 1, 'mollis': 1,
 'molestie': 2, 'pellentesque': 1, 'cursus': 1, 'lacus': 1, 'rhoncus': 2,
 'diam': 1, 'erat': 1, 'libero': 1, 'enim': 1, 'nulla': 1, 'potenti': 1,
 'vestibulum': 1, 'turpis': 1, 'magna': 1, 'duis': 1, 'luctus': 1,
 'aliquam': 1, 'hendrerit': 1}

>>> dos.ordenar_diccionario({diego:0, john:34, superhijitus: 9999, roy:desaprueba, amalia:-1})
{amalia:-1, diego:0, john:34, superhijitus:9999, roy:desaprueba}
"""
#etapa 3
"""
"""

#etapa 4
"""
"""

#-----------------------------------------------------------------------------#

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
        
        
def main():
    doctest.testmod()
main()