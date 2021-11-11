letras_desacertadas = []
letras_acertadas = []

palabra = "casa"

def palabra_adivinada():
    """Decide si la palabra ya ha sido adivinada
    Autor: Ignacio Oroná"""
    rv = True

    for letra in palabra:
        if letra not in letras_acertadas:
            rv = False

    return rv

def dame_palabra_secreta(pal):
    """Cambia las letras no acertadas en la palabra por ?
    Autor: Ignacio Oroná"""
    rv = ''
    for letra in palabra:
        if letra in letras_acertadas:
            rv += letra
        else:
            rv += '?'

    return rv

def dame_desaciertos():
    """Devuelve una string con las letras desacertadas para mostrar el el display
    Autor: Ignacio Oroná"""
    rv = ''
    for a in letras_desacertadas:
        rv += a

    return str(len(letras_desacertadas)) + ' - ' + rv

def mostrar_estado_actual():
    """Muestra el estado de la partida
    Autor: Ignacio Oroná"""
    print("Palabra a adivinar: ", dame_palabra_secreta(palabra), "Aciertos:", len(letras_acertadas), "Desaciertos:", dame_desaciertos())


def terminar_juego(estado_juego):
    """Termina el juego dadas las condiciones de la consigna
    Autor: Ignacio Oroná"""
    rv = estado_juego

    if len(letras_desacertadas) > 6 or palabra_adivinada():
        rv = True

    return rv

def procesar_letra(letra):
    """Agrega la letra a la lista de letras acertadas o desacertadas
    Autor: Ignacio Oroná"""
    if letra_ingresada in palabra:
        if letra_ingresada not in letras_acertadas:
            letras_acertadas.append(letra_ingresada)
        else:
            print("Letra ya ingresada")
    else:
        if letra_ingresada not in letras_desacertadas:
            letras_desacertadas.append(letra_ingresada)


mostrar_estado_actual()
estado_juego = False

while(terminar_juego(estado_juego) == False):
    letra_ingresada = input("Ingresa Letra:")

    if letra_ingresada in ("FIN","0"):
        estado_juego = True
    elif not letra_ingresada.isalpha() or len(letra_ingresada) > 1 or letra_ingresada == "ª":
        print("Ingreso invalido")
    else:
        procesar_letra(letra_ingresada)
        mostrar_estado_actual()

print("FIN")