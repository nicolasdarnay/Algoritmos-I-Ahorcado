def calcular_puntos(aciertos, desaciertos, acumulado):
    """Calcula el puntaje de la partida
    Autores: Federico Castillo / Francisco Albinati
    """
    rv = aciertos * 10 + desaciertos * (-5)

    return rv


def seguir_jugando():
    """Pregunta al usuario si quiere jugar otra partida
    Autores: Federico Castillo / Francisco Albinati
    """
    peticion = input("¿Desea seguir jugando? si/no: ")
    while peticion not in ("si","no"):
        peticion = input("Por favor, responda con si/no: ") 
        
    return peticion == "si"
