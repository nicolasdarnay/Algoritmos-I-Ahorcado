import tp_parte_2 as dos
import tp_parte_4 as cuatro
import tp_parte_5 as cinco
import tp_parte_8 as ocho
import os
import time
import estados
import random
import time
import getopt, sys
import doctest
from copy import deepcopy

ESTADOS = estados.estado()
DICCIONARIO = None
EXCEPCION = "ª"
ACIERTO = 0
DESACIERTO = 1
MAX_DESACIERTOS = 6

# Constantes
DICCIONARIO = None
EXCEPCION = "ª"
ACIERTO = 0
DESACIERTO = 1

ACIERTOS_PARTIDO = 0
DESACIERTOS_PARTIDO = 1
PUNTAJE_PARTIDO = 2
ACIERTOS_TOTALES = 3
DESACIERTOS_TOTALES = 4
PUNTAJE_TOTAL = 5
CANT_PARTIDAS = 6
CANT_PARTIDOS_GANADOS = 7
PALABRA = 8

CANTIDAD_MAXIMA_DESACIERTOS = 7

MODO_NORMAL = 0
MODO_DEBUG = 1
MODO_TEST = 2

JUGADOR = 0
PUNTAJE = 1
PARTIDOS_GANO = 2
ACERTO_TOTALMENTE = 3
DESACERTO_TOTALMENTE = 4

CONFIG_SUMAR = 0
CONFIG_RESTAR = 1
CONFIG_ADIVINO = 2
CONFIG_MAX_USUARIOS = 3
CONFIG_MAX_DESACIERTOS = 4
CONFIG_GANO_PC = 5
CONFIG_LONG_MIN = 6
CONFIG_DICC = 7


VALORES_DEFECTO = {"MAX_USUARIOS": 3,
                   "LONG_PALABRA_MIN": 10,
                   "MAX_DESACIERTOS": 7,
                   "PUNTOS_ACIERTOS": 10,
                   "PUNTOS_DESACIERTOS": 5,
                   "PUNTOS_ADIVINA_PALABRA": 100,
                   "PUNTOS_RESTA_GANA_PROGRAMA": 20}


def cargar_configuracion():
    configuracion = ocho.establecer_configuracion(VALORES_DEFECTO)
    sumar = configuracion["PUNTOS_ACIERTOS"]
    restar = configuracion["PUNTOS_DESACIERTOS"]
    adivino = configuracion["PUNTOS_ADIVINA_PALABRA"]
    max_usuarios = configuracion["MAX_USUARIOS"]
    max_desaciertos = configuracion["MAX_DESACIERTOS"]
    gano_pc = configuracion["PUNTOS_RESTA_GANA_PROGRAMA"]
    long_minima = configuracion["LONG_PALABRA_MIN"]
    return (sumar, restar, adivino, max_usuarios, max_desaciertos,gano_pc, long_minima, configuracion)

def limpiar_pantalla():
    """
    Borra la pantalla
    Autor: Ignacio Orona
    """
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def palabra_adivinada(palabra, acertadas):
    """
    >>> palabra_adivinada("hola", ['h', 'o', 'l', 'a'])
    True
    >>> palabra_adivinada("chau", ['c', 'h', 'a'])
    False
    """
    """
    Devuele si la palabra fue adivinada o no
    Autor Ignacio Orona
    """
    rv = True
    for letra in palabra:
        if letra not in acertadas:
            rv = False
    return rv

def dame_palabra_secreta(palabra, acertadas):
    """
    >>> dame_palabra_secreta('palabra', 'xyz') == '???????'
    True
    >>> dame_palabra_secreta('palabra', 'a') == '?a?a??a'
    True
    >>> dame_palabra_secreta('palabra', 'pal') == 'pala??a'
    True
    """
    """
    Devuelve in String con la palabra secreta con los ? intercalados
    Autor Ignacio Orona
    """
    rv = ''
    for letra in palabra:
        if letra in acertadas:
            rv += letra
        else:
            rv += '?'
    return rv

def dame_desaciertos(desacertadas):
    """
    >>> dame_desaciertos('abcd')
    '4 - abcd'
    >>> dame_desaciertos('xyz')
    '3 - xyz'
    """
    """
    Devuele el string con la letras con desaciertos
    Autor: Ignacio Orona
    """
    rv = ''
    for a in desacertadas:
        rv += a
    return str(len(desacertadas)) + ' - ' + rv

def mostrar_estado_actual(palabra, acertadas, desacertadas, jugador, puntaje_parcial):
    """
    >>> mostrar_estado_actual('contingencia', 'aei', 'xyz', 'uno', 0)
    'Palabra a adivinar: ????i??e??ia. Aciertos: 3. Desaciertos: 3 - xyz. Turno actual: uno. Puntaje parcial: 0'
    """
    """
    Esta funcion dibuja el estado actual del juego
    Autor: Ignacio Chacon
    """
    limpiar_pantalla()
    mostrada = dame_palabra_secreta(palabra, acertadas)
    aciertos = len(acertadas)
    desaciertos = dame_desaciertos(desacertadas)
    res = f"Palabra a adivinar: {mostrada}. Aciertos: {aciertos}. Desaciertos: {desaciertos}. Turno actual: {jugador}. Puntaje parcial: {puntaje_parcial}"
    return res
def terminar_juego(palabra, acertadas, desacertadas, lista, jugador, rv = False):
    """
    >>> terminar_juego('prestidigitador', 'aei', 'xyz', ['uno', 'dos', 'tres'], 'uno')
    True
    """
    """
    Esta función indica si hay que terminar el juego o no
    Autor: Ignacio Orona
    """
    DESACIERTOS = len(desacertadas)
    if DESACIERTOS > 0 or palabra_adivinada(palabra, acertadas):
        rv = True
    if DESACIERTOS !=0 and ultima_es_0_fin(desacertadas):
        rendirse(lista, jugador)
        rv = True
    return rv


def ultima_es_0_fin(desacertadas):
    """
    >>> ultima_es_0_fin('FIN')
    False
    >>> ultima_es_0_fin('0')
    True
    >>> ultima_es_0_fin('s')
    False
    >>> ultima_es_0_fin('a')
    False
    """
    """
    Devuelve True/False si es que el usuario ingreso 0 o FIN
    Autor: Ignacio Orona
    """
    if len(desacertadas) == 0:
        rv = False
    else:
        rv = desacertadas[-1] in ("0","FIN")

    return rv

def rendirse(lista, jugador):
    """
    >>> rendirse(['uno', 'dos', 'tres'], 'dos')
    dos se ha rendido.
    Recibe una penalización de -30 puntos!
    Removiendo a dos
    ['uno', 'tres']
    """
    """
    Retira al jugador que haya tomado la desición de rendirse y
    lo penaliza.
    Autor: Nicolás Darnay
    """
    print(f"{jugador} se ha rendido.\nRecibe una penalización de -30 puntos!\nRemoviendo a {jugador}")
    time.sleep(3.5)
    lista.remove(jugador)
    return lista

def se_rindio():
    """
    Si se rinde, se imprime un mensaje advirtiendo de la penalización
    Autor: Nicolás Darnay
    """
    limpiar_pantalla()
    print("Usted se ha rendido, por ende fue penalizado (-5 puntos)")
    time.sleep(1.5)


def procesar_letra(letra, palabra, acertadas, desacertadas, config):
    """
    >>> procesar_letra('a', 'iscoceles', [], [])
    -1
    >>> procesar_letra('b', 'bueno', ['u','e','o'], ['x', 'y', 'z'])
    2
    """
    """
    Se fija si la letra fue ingresada o no y maneja segun el caso
    devuelve el puntaje que resulta
    Autores: Ignacio Orona
    """
    rv = 0
    if letra in palabra:
        if letra not in acertadas:
            acertadas.append(letra)
            rv += config[CONFIG_SUMAR]
        else:
            print("Letra ya ingresada")
            time.sleep(1.5)
    else:
        if letra not in desacertadas and letra in ('0', 'FIN'):
            rv = config[CONFIG_RESTAR]
            desacertadas.append(letra)
        elif letra not in desacertadas:
            rv = config[CONFIG_RESTAR]
            desacertadas.append(letra)
        else:
            print("Letra ya ingresada")
            time.sleep(1.5)
    return rv

def ingreso_de_letras(palabra, acertadas, desacertadas, conf):
    """
    Decide si la letra ingresada es invalida o no
    y devuelve puntaje
    Autor: Ignacio Orona
    """
    rv = 0
    letra_ingresada = input("Ingresa Letra: ")
    if letra_ingresada in ("FIN","0"):
        rv = procesar_letra(letra_ingresada, palabra, acertadas, desacertadas, conf)
    elif not letra_ingresada.isalpha() or len(letra_ingresada) > 1 \
    or letra_ingresada == EXCEPCION:
        print("Ingreso invalido")
        time.sleep(1.5)
    else:
        rv = procesar_letra(letra_ingresada, palabra, acertadas, desacertadas, conf)
    return rv

def cargar_diccionario():
    """
    Carga el diccionario en memoria
    Autor: Ignacio Orona
    """
    limpiar_pantalla()

    print("Bienvenido a Ahorcado (2.0.1) Por favor espere...")
    return dos.obtener_diccionario()


def ingresarJugadores(max_jugadores):
    """
    Maneja el ingreso de cada jugador.
    Autores: Ignacio Orona & Nicolás Darnay"
    """
    ingreso = ""
    res = []
    while (ingreso != "" or len(res) < 1) and len(res) < max_jugadores:
        ingreso = anadir_jugador(res)
        if ingreso != "": res.append(ingreso)
    return res

def anadir_jugador(ya_ingresados):
    """
    Maneja el input de jugadores.
    Autor: Nacho Chacon & Nicolas Darnay
    """
    res = input("Por favor ingrese el nombre del jugador: ")
    if len(res) > 0:
        while res == "" or res in ya_ingresados:
            res = input("Ya ha ingresado ese jugador: ")
    return res

def presentar_orden_jugadores(jugadores):
    """
    >>> presentar_orden_jugadores(['uno', 'dos', 'tres'])
    Bienvenido al juego de Ahorcardo, el orden de los jugadores será (a saber):
    uno
    dos
    tres
    """
    """
    Esta funcion simplemente muestra el orden de los jugadores
    Autor: Ignacio Orona & Nicolas Darnay
    """
    print("Bienvenido al juego de Ahorcardo, el orden de los jugadores será (a saber):")
    for jugador in jugadores:
        print(jugador)



def inicializar_juego(jugadores, diccionario, modo):
    """
    Esta funcion setea como se necesita incialmente
    la estructura de datos que lleva el juego
    Autor: Ignacio Orona & Nicolas Darnay
    """
    res = {}
    for jugador in jugadores:
        res[jugador] = ([], [], 0, 0, 0, 0, 0, 0, '')

    return res

def actualizar_palabra(jugadores, palabra, diccionario, modo, juego):
    """
    Actualiza el diccionario del juego con la nueva palabra sorteada
    Autor: Ignacio Orona & Nicolas Darnay
    """
    for jugador in jugadores:
        dicc = juego[jugador]
        nueva_palabra = cuatro.palabra_con_longitud(diccionario, len(palabra))
        if modo == MODO_DEBUG:
            print("Palabra para", jugador, "es palabra:", nueva_palabra)

        juego[jugador] = ([], # ACIERTOS_PARTIDO
                          [], # DESACIERTOS_PARTIDO
                          0,  # PUNTAJE_PARTIDO
                          dicc[ACIERTOS_TOTALES],
                          dicc[DESACIERTOS_TOTALES],
                          dicc[PUNTAJE_TOTAL],
                          dicc[CANT_PARTIDAS],
                          dicc[CANT_PARTIDOS_GANADOS],
                          nueva_palabra)

    return juego

def mostrar_puntaje_parcial(juego, jugadores, jugador, gano):
    """
    Esta función le muestra al usuario el puntaje parcial
    entre otros datos
    Autor: Ignacio Orona & Nicolas Darnay
    """
    if gano:
        print(f"¡¡¡¡ Ganador/a es {jugador} !!!!!!")
    else:
        print("Gano la PC!")
    for jugador in juego:
        tupla_juador = juego[jugador]
        print(f"El jugador, {jugador} termino con {tupla_juador[PUNTAJE_PARTIDO]} puntos. Su palabra era: '{tupla_juador[PALABRA]}'. Aciertos: {len(tupla_juador[ACIERTOS_PARTIDO])} Desaciertos: {len(tupla_juador[DESACIERTOS_PARTIDO])}")

def mostrar_puntaje_final(juego, jugadores, jugador, gano):
    """
    Esta función muestra el puntaje final con sus
    respectivos aciertos y errores mostrando primero
    los jugadores con mayor puntaje
    Autor: Ignacio Orona & Nicolas Darnay
    """
    cant_partidos_totales = 0
    list_jugadores = []
    print("**************************************** Esto es todo amigos!!!! **************************************************")
    for jugador in juego:
        tupla_jugador = juego[jugador]
        cant_partidos_totales = max(cant_partidos_totales, tupla_jugador[CANT_PARTIDAS])
        nuevo_elemento = (jugador, tupla_jugador[PUNTAJE_TOTAL], tupla_jugador[CANT_PARTIDOS_GANADOS], tupla_jugador[ACIERTOS_TOTALES], (tupla_jugador[DESACIERTOS_TOTALES]))
        list_jugadores.append(nuevo_elemento)

    list_jugadores.sort(key = lambda item : item[1], reverse=True)

    for jugador in list_jugadores:
        print(f"* El jugador, {jugador[JUGADOR]} termino con {jugador[PUNTAJE]} puntos. Gano {jugador[PARTIDOS_GANO]} partidos. Aciertos Totales: {jugador[ACERTO_TOTALMENTE]}. Desaciertos Totales:  {jugador[DESACERTO_TOTALMENTE]} ")
    print(f" (Se jugaron {cant_partidos_totales} partidos en total)")
    print("*******************************************************************************************************************")

def ordenar_jugadores(jugadores, gano, turno, ganador = None):
    """
    Ordena aleatoriamente a los jugadores. Si hubo un
    ganador en la partida anterior lo pone al frente
    Autor: Ignacio Orona
    """
    if gano:
        random.shuffle(jugadores)
        pos_ganador = jugadores.index(ganador)
        aux = jugadores[0]
        jugadores[0] = jugadores[pos_ganador]
        jugadores[pos_ganador] = aux
    else:
        random.shuffle(jugadores)
    return jugadores

def main(modo):
    """
    Main del programa. Maneja todas las partidos, juegos
    la magia esta aca
    Autores: Ignacio Orona & Nicolas Darnay
    """
    configuracion = cargar_configuracion()
    jugadores = []
    DICCIONARIO = cargar_diccionario()
    JUGADORES = ingresarJugadores(configuracion[CONFIG_MAX_USUARIOS])
    juego = inicializar_juego(JUGADORES, DICCIONARIO, modo)

    otra_partida = True
    gano = None
    turno = None
    ganador = None

    while otra_partida:
        configuracion = cargar_configuracion()
        ocho.mostrar_configuracion(configuracion[CONFIG_DICC], VALORES_DEFECTO)

        jugadores = deepcopy(JUGADORES)
        ordenar_jugadores(jugadores, gano, turno, ganador)
        presentar_orden_jugadores(jugadores)
        palabra = cuatro.palabra(DICCIONARIO)
        juego = actualizar_palabra(jugadores, palabra, DICCIONARIO, modo, juego)

        gano = False
        estado_juego = True
        turno = 0
        
        while estado_juego:
            jugador = jugadores[turno]
            tupla_juego = juego[jugador]
            puntaje_parcial = 0
            palabra = tupla_juego[PALABRA]

            desacertadas = tupla_juego[DESACIERTOS_PARTIDO]
            acertadas = tupla_juego[ACIERTOS_PARTIDO]
            desacertadas_este_juego = []

            puntaje_total = tupla_juego[PUNTAJE_TOTAL]
            cantidad_partidos_jugados = tupla_juego[CANT_PARTIDAS]
            cantidad_partidos_ganados = tupla_juego[CANT_PARTIDOS_GANADOS]

            print(mostrar_estado_actual(palabra, acertadas, desacertadas, jugador, puntaje_parcial))

            while not terminar_juego(palabra, acertadas, desacertadas_este_juego, jugadores, jugador):
                puntaje_parcial += ingreso_de_letras(palabra, acertadas, desacertadas_este_juego, configuracion)
                print(mostrar_estado_actual(palabra, acertadas, desacertadas_este_juego+desacertadas, jugador, puntaje_parcial))

            if palabra_adivinada(palabra, acertadas):
                gano = True
                puntaje_parcial += configuracion[CONFIG_ADIVINO]
                cantidad_partidos_ganados += 1
                cantidad_partidos_jugados += 1
                estado_juego = False
            else:
                puntaje_parcial -= 5

            if len(desacertadas_este_juego)+len(desacertadas) >= CANTIDAD_MAXIMA_DESACIERTOS:
                if modo == MODO_DEBUG:
                    print(f"Removiendo al jugador: {jugador}")
                jugadores.remove(jugador)
                turno -= 1
                time.sleep(1.5)
                cantidad_partidos_jugados += 1

            if len(jugadores) < 1:
                estado_juego = False

            puntaje_total += puntaje_parcial

            aciertos_totales = tupla_juego[ACIERTOS_TOTALES]+len(acertadas)
            desaciertos_totales = tupla_juego[DESACIERTOS_TOTALES]+len(desacertadas_este_juego)

            juego[jugador] = (acertadas,                            # ACIERTOS_PARTIDO
                              desacertadas+desacertadas_este_juego, # DESACIERTOS_PARTIDO
                              puntaje_parcial,                      # PUNTAJE_PARTIDO
                              aciertos_totales,                     # ACIERTOS_TOTALES
                              desaciertos_totales,                  # DESACIERTOS_TOTALES
                              puntaje_total,                        # PUNTAJE_TOTAL
                              cantidad_partidos_jugados,            # CANT_PARTIDAS_JUGADAS = 7
                              cantidad_partidos_ganados,            # CANT_PARTIDOS_GANADOS = 8
                              palabra)                              # PALABRA
            if gano != True:
                turno = 0 if (turno+1) >= len(jugadores) else turno + 1
            else:
                ganador = jugadores[turno]

        mostrar_puntaje_parcial(juego, jugadores, jugador, gano)
        otra_partida = cinco.seguir_jugando()

    mostrar_puntaje_final(juego, jugadores, jugador, ganador)


argumentList = sys.argv[1:]
options = "td"
long_options = ["test", "debug"]
arguments, values = getopt.getopt(argumentList, options, long_options)

if len(arguments) == 0:
    main(MODO_NORMAL)
else:
    for currentArgument, currentValue in arguments:
        if currentArgument in ("-t", "--test"):
            print(doctest.testmod())
        elif currentArgument in ("-d", "--debug"):
            main(MODO_DEBUG)


