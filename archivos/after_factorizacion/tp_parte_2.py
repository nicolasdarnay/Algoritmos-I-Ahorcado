import texto as t

LONGITUD_MINIMA = 4

#isalpha() toma esto como letra del alfabeto
EXCEPCION = "ª"

#ordena el diccionario de forma ascendente
ordenar_diccionario = lambda diccionario: dict(sorted(diccionario.items()))


"""
REGLAS:
    - Se elimina toda palabra con caracteres numéricos
    - Al momento de ordenar el diccionario, se asume que ninguna
    palabra contiene caracteres extranjeros al inglés o al español (è,ò,etc.)
    -Se separan palabras )juntas_de:esta.manera;.
"""


def es_valida(palabra):
    """Devuelve un booleano que indica si la palabra se puede anadir
    al diccionario o no
    Autor: Ignacio Chacón"""
    rv = True
    for caracter in palabra:
        if not caracter.isalpha() or caracter == EXCEPCION:
            rv = False
    if len(palabra) < LONGITUD_MINIMA: 
        rv = False
    return rv


def eliminar_invalidos_internos(lista):
    """Elimina los caracteres invalidos de una lista de caracteres.
    Autor: Ignacio Chacón"""
    rv = []
    for caracter in lista:
        if caracter.isalpha():
            rv.append(caracter)
        else:
            rv.append(" ")
    return rv


def limpiar_palabra(palabra):
    """ Separa las palabras que poseen invalidos de por medio.
    Autor: Ignacio Chacón"""
    lista_de_caracteres = list(palabra)
    rv = ""
    caracteres_validos = eliminar_invalidos_internos(lista_de_caracteres)
    for caracter in caracteres_validos:
        rv += caracter
    return rv.split()


def limpiar_lista(lista):
    """ Aplica los metodos definidos en una lista de palabras.
    Autor: Ignacio Chacón"""
    rv = []
    PRETRADUCCION = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u", "ñ":"n"}
    for palabras in lista:
        palabras = limpiar_palabra(palabras.lower())
        for palabra in palabras:
            traduccion = palabra.maketrans(PRETRADUCCION)
            palabra = palabra.translate(traduccion)
            rv.append(palabra)
    return rv


def conseguir_palabras_validas(texto):
    """Añade las palabras validas y la cantidad de veces que aparecen en el
    texto al diccionario.
    Autor: Ignacio Chacón"""
    diccionario = {}
    lista_de_palabras = limpiar_lista(texto.split())
    for palabra in lista_de_palabras:
        if not palabra in diccionario.keys() and es_valida(palabra):
            valor_asociado = lista_de_palabras.count(palabra)
            diccionario.update({palabra:valor_asociado})
    return diccionario

            
def obtener_diccionario(texto):
    """Genera un diccionario ordenado con todas las palabras de un texto
    asociadas al numero de veces que aparecen.
    Autor: Ignacio Chacón"""
    texto = t.obtener_texto()
    diccionario = conseguir_palabras_validas(texto)
    diccionario = ordenar_diccionario(diccionario)
    return diccionario
  
    
def main():
    "Main del programa, imprime el diccionario de forma ordenada"
    diccionario_de_palabras = obtener_diccionario()
    for key in diccionario_de_palabras:
        print(f"{key}, {diccionario_de_palabras[key]}")
    print("Hay", len(diccionario_de_palabras), "palabras validas diferentes en el texto")
    print("\n")
#main()