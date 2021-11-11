from time import sleep
import tp_parte_2 as dos
from pathlib import Path
from random import choice

ARCHIVO_1 = open("cuentos.txt")
ARCHIVO_2 = open("la_arana.txt")
ARCHIVO_3 = open("noches.txt")
ARCHIVOS = [ARCHIVO_1,ARCHIVO_2,ARCHIVO_3]


def leer_linea_csv(archivo):
    """lee linea de csv. Devuelve lista con sus componentes. 
    Autores: Francisco Albinatti, Ignacio Chacón"""
    linea = archivo.readline()
    if linea:
        rv = linea.rstrip("\n").split(",")
    else:
        rv = None
    return rv


def leer_linea_txt(archivo):
    """lee linea de csv. Devuelve lista con sus componentes. 
    Autores: Francisco Albinatti, Ignacio Chacón"""
    linea = archivo.readline()
    if linea:
        rv = linea.rstrip("\n").split()
    else:
        rv = None
    return rv


def modificar_valor(variable, valor_variable, por_defecto):
    "Actualiza un valor del diccionario. Autores: Albinatti, Chacon"
    rv = por_defecto.copy()
    if variable in por_defecto and por_defecto[variable] != valor_variable:
        rv[variable] = int(valor_variable)
    else:
        rv[variable] = int(valor_variable)
    return rv
        

def establecer_configuracion(por_defecto):
    """Manejo del archivo configuracion.csv. Retorna u diccionario con
    los valores de la configuracion"""
    CONFIGURACION = open("configuracion.csv")
    NOMBRE_VARIABLE = 0
    VALOR_VARIABLE = 1
    linea = leer_linea_csv(CONFIGURACION)
    rv = por_defecto.copy()
    while linea:
        variable = linea[NOMBRE_VARIABLE]
        valor = linea[VALOR_VARIABLE]
        rv = modificar_valor(variable, valor, rv)
        linea = leer_linea_csv(CONFIGURACION)
    CONFIGURACION.close()
    return rv
        

def mostrar_configuracion(configuracion, por_defecto):
    """Muestra la configuracion y de donde provienen los valores
    Autores: Francisco Albinatti, Ignacio Chacon"""
    for variable in configuracion:
        valor = configuracion[variable]
        if valor != por_defecto[variable]:
            print(f"{variable} vale {valor} y fue dado por el archivo")
        else:
            print(f"{variable} vale {valor} y es el valor por defecto")
    sleep(5)
    

def actualizar_palabras(palabras, rv, indice):
    """Interior del manejo de los archivos de texto. Recibe las palabras
    validas de una linea, devuelve el diccionario actualizado.
    Autores: Francisco Albinatti, Ignacio Chacon"""
    for palabra in palabras:
        if palabra not in rv:
            valores = [0 for numero in range(0,len(ARCHIVOS))]
            rv.update({palabra:valores})
            rv[palabra][indice] += 1
        else:
            rv[palabra][indice] += 1
    return rv     


def obtener_diccionario_primera():
    """Obtiene un diccionario la primera vez que se ejecuta la aplicacion
    Autores: Francisco Albinatti, Ignacio Chacon"""
    LINEAS = [leer_linea_txt(archivo) for archivo in ARCHIVOS]
    rv = {}
    while LINEAS != [None for archivo in ARCHIVOS]:
        for linea in LINEAS:
            if linea != None:
                indice = LINEAS.index(linea)
                palabras = dos.limpiar_lista(linea)
                actualizar_palabras(palabras, rv, indice)
        LINEAS = [leer_linea_txt(archivo) for archivo in ARCHIVOS]
    return dos.ordenar_diccionario(rv)


def obtener_lista(long_minima):
    """Obtiene una lista con las palabras con longitud deseada del archivo.
    Autores: Francisco Albinatti, Ignacio Chacon"""
    rv = []
    PALABRA = 0
    with open("palabras.csv") as palabras:
        linea = leer_linea_csv(palabras)
        while linea:
            if len(linea[PALABRA]) >= long_minima:
                rv.append(linea[PALABRA])
            linea = leer_linea_csv(palabras)
    return rv


def crear_linea(diccionario, palabra):
    "Formato de la linea para palabras.csv. Autores: Albinatti, Chacon"
    rv = f"{palabra}"
    for valor_asociado in diccionario[palabra]:
        rv += f",{valor_asociado}"
    rv += "\n"
    return rv


def guardar_palabras(diccionario):
    "Guarda los datos del diccionario en palabras.csv. Autores: Albinatti, Chacon"
    with open("palabras.csv","w") as palabras:
        for palabra in diccionario:
            linea = crear_linea(diccionario,palabra)
            palabras.write(linea)
            
            
def si_existe_obtener(long_minima):
    """Si es la primera vez que el usuario entra ejecuta las funciones
    para guardar datos en palabras.csv y devuelve las palabras.
    Si ya existe palabras.csv lee directamente de ahi
    Autores: Francisco Albinatti, Ignacio Chacon"""
    existe = Path.exists(Path("palabras.csv"))
    if existe:
        rv = obtener_lista(long_minima)
    else:
        diccionario = obtener_diccionario_primera(long_minima)
        guardar_palabras(rv)
        rv = list(diccionario.keys())
    return rv


def palabra(lista,long_minima):
    "Devuelve una palabra con la long_buscada. Autor: Ignacio Chacon"
    lista = [palabra for palabra in lista if len(palabra) >= long_minima]
    return choice(lista)


ARCHIVO_1.close()
ARCHIVO_2.close()
ARCHIVO_3.close()