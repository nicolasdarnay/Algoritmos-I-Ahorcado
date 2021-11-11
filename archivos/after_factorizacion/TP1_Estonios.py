import tp_parte_2 as dos
import tp_parte_4 as cuatro
import tp_parte_5 as cinco
import os
import time
import estados

ESTADOS = estados.estado()
DICCIONARIO = None
EXCEPCION = "ª"
ACIERTO = 0
DESACIERTO = 1
MAX_DESACIERTOS = 6


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
    "Devuele si la palabra fue adivinada o no. Autor Ignacio Orona"
    rv = True
    for letra in palabra:
        if letra not in acertadas:
            rv = False
    return rv


def dame_palabra_secreta(palabra, acertadas):
    """
    Devuelve un String con la palabra secreta con los ? intercalados
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
    Devuele el string con la letras con desaciertos
    Autor Ignacio Orona
    """
    rv = ''
    for a in desacertadas:
        rv += a
    return str(len(desacertadas)) + ' - ' + rv


def mostrar_estado_actual(palabra, acertadas, desacertadas):
    """
    Esta funcion dibuja el estado actual del juego
    Autor Ignacio Chacon
    """
    limpiar_pantalla()
    mostrada = dame_palabra_secreta(palabra, acertadas)
    aciertos = len(acertadas)
    desaciertos = dame_desaciertos(desacertadas)
    print("Palabra a adivinar: ", mostrada, "Aciertos:", aciertos, "Desaciertos:", desaciertos)
    print(ESTADOS[len(desacertadas)], "\n")


def terminar_juego(palabra, acertadas, desacertadas, rv = False):
    """
    Esta función indica si hay que terminar el juego o no
    Autor: Ignacio Orona
    """
    DESACIERTOS = len(desacertadas)
    if DESACIERTOS > MAX_DESACIERTOS or palabra_adivinada(palabra, acertadas):
        rv = True
        if DESACIERTOS > MAX_DESACIERTOS:
        	print("La palabra era", palabra)
        	time.sleep(1.5)
    elif DESACIERTOS != 0 and ultima_es_0_fin(desacertadas):
        se_rindio()
        print("La palabra era", palabra)
        time.sleep(1.5)
        rv = True
    return rv


def ultima_es_0_fin(desacertadas):
    """
    Devuelve True/False si es que el usuario ingreso 0 o FIN
    Autor Ignacio Orona
    """
    if len(desacertadas) == 0:
        rv = False
    else:
        rv = desacertadas[-1] in ("0","FIN")

    return rv


def se_rindio():
    """
    Si se rinde, se imprime un mensaje advirtiendo de la penalización
    Autor: Nicolás Darnay
    """
    limpiar_pantalla()
    print("Usted se ha rendido, por ende fue penalizado (-5 puntos)")
    time.sleep(1.5)


def procesar_letra(letra, palabra, acertadas, desacertadas):
    """
    Se fija si la letra fue ingresada o no y maneja segun el caso
    Autor Ignacio Orona
    """
    if letra in palabra:
        if letra not in acertadas:
            acertadas.append(letra)
        else:
            print("Letra ya ingresada")
            time.sleep(1.5)
    else:
        if letra not in desacertadas:
            desacertadas.append(letra)
        else:
        	print("Letra ya ingresada")
        	time.sleep(1.5)


def ingreso_de_letras(palabra, acertadas, desacertadas):
    """
    Decide si la letra ingresada es invalida o no.
    Autor: Ignacio Orona
    """
    letra_ingresada = input("Ingresa Letra: ")
    if letra_ingresada in ("FIN","0"):
        procesar_letra(letra_ingresada, palabra, acertadas, desacertadas)
    elif not letra_ingresada.isalpha() or len(letra_ingresada) > 1 \
    or letra_ingresada == EXCEPCION:
        print("Ingreso invalido")
        time.sleep(1.5)
    else:
        procesar_letra(letra_ingresada, palabra, acertadas, desacertadas)
        

def jugar_partida(palabra):
    """Genera una partida para que el usuario juegue y devuelve su puntaje
    en ella. Autor: Ignacio Chacon"""
    desacertadas = []
    acertadas = []
    mostrar_estado_actual(palabra, acertadas, desacertadas)
    
    while not terminar_juego(palabra, acertadas, desacertadas):
        ingreso_de_letras(palabra, acertadas, desacertadas)
        mostrar_estado_actual(palabra, acertadas, desacertadas)
        
    desaciertos = len(desacertadas)
    aciertos = len(acertadas)
    return aciertos, desaciertos


def cargar_diccionario():
    "Carga el diccionario en memoria. Autor: Ignacio Orona"
    limpiar_pantalla()
    print("Bienvenido a Ahorcado™ (1.0.0) Por favor espere...")
    return dos.obtener_diccionario()


def seguir_jugando():
    """Pregunta al usuario si quiere jugar otra partida
    Autores: Federico Castillo / Francisco Albinati
    """
    peticion = input("¿Desea seguir jugando? si/no: ")
    while peticion not in ("si","no"):
        peticion = input("Por favor, responda con si/no: ") 
    return peticion == "si"


def main():
    "Main del programa. Autor: Ignacio Orona"
    otra_partida = True
    puntaje = 0
    DICCIONARIO = cargar_diccionario()
    while otra_partida:
    	limpiar_pantalla()
    	print("Puede salir de la partida con 0 o FIN")
    	time.sleep(1.5)
    	puntos = jugar_partida(cuatro.palabra(DICCIONARIO))
    	puntaje += puntos[ACIERTO] * 10 + puntos[DESACIERTO] * (-5)
    	otra_partida = seguir_jugando()
    print("Su puntaje final es:", puntaje)
    print("Gracias por jugar ☺")

main()