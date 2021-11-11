Objetivo
Construir un programa en etapas, que permita jugar al ahorcado, teniendo en cuenta
las reglas que más adelante se detallan.
Entregas
El Trabajo Práctico está dividido en dos partes. Ambas tendrán una fecha de entrega
establecida y es requisito necesario aprobarlas en tiempo y forma; para así poder
continuar con la materia y aprobarla.
La primera parte deberá ser entregada a través del campus, y cumpliendo las
condiciones establecidas, y su fecha de vencimiento será el 8 de junio 2021.
La segunda parte agregará nuevas etapas de construcción a la primera entrega, y su
fecha de entrega será informada oportunamente, así como la descripción narrativa
de las funcionalidades que se sumarán.
Descripción de las Etapas de la Parte 1
La parte 1 está formada por 5 etapas de desarrollo. Esta división en etapas, es para
ayudarlos en la organización del diseño y desarrollo total del trabajo. Se les sugiere
ir cumpliendo con cada una de las etapas, a medida que hayamos abordado los
temas conceptuales que involucran a la etapa, siguiendo las pautas descriptas, y
tratando de realizar al menos una etapa por semana.
Si nunca has jugado al ahorcado, es recomendable que busques una versión para
jugar en línea, y dediques un instante a jugar.
Ten en cuenta que las reglas que estableceremos a continuación, podrían diferir de
las cuales vos hayas jugado.
Etapa 1 - Interacción con el Jugador
En esta etapa deberás escribir las funciones que consideres necesarias, y que
permitan una interacción con el jugador, y que sigan los lineamientos que se dan a
continuación.
Inicialmente, comenzaremos por mostrar tantos signos de preguntas como letras
componen la palabra a adivinar, y a continuación pediremos el ingreso de una letra.
Supongamos que la palabra a adivinar es “naranja”, veremos algo parecido a lo
siguiente:
 Palabra a adivinar: ??????? Aciertos: 0 Desaciertos: 0
 Ingrese Letra: _ 

Un jugador puede tener como máximo 7 desaciertos por palabra a adivinar, de tal
modo que el jugador ganará si adivinó la palabra y tuvo menos de 8 desaciertos, o
perderá si llegó al 8vo. desacierto.
En cada interacción se debe pedir al jugador el ingreso de una letra, si la letra se
encuentra en la palabra a adivinar, se debe mostrar en las posiciones que se
encuentra, por ejemplo: si la palabra a adivinar es “naranja” y el jugador ingresó la
letra “a”, entonces se debe mostrar:
 Muy bien!!! → ?a?a??a Aciertos: 1 Desaciertos: 0
 Ingrese Letra: _
A continuación se debe solicitar el ingreso de otra letra. Si el jugador vuelve a
ingresar una “a”, debería recibir un mensaje de “Letra ya ingresada”.
Si la letra ingresada por el jugador es una letra inexistente en la palabra, entonces,
se debe sumar su desacierto y además mostrar a continuación de la cantidad la
cadena de las letras desacertadas; por ejemplo, si ingresó una “p”:
 Lo siento!!! → ?a?a??a Aciertos: 1 Desaciertos: 1 - p
 Ingrese Letra: _
Note que a continuación de la cantidad de desaciertos, deben mostrarse las letras
que el jugador fue ingresando y que no forman parte de la palabra.
Los ingresos de letras deberían terminar ó porque se alcanzó la cantidad máxima de
desaciertos, ó porque el jugador adivinó la palabra.
También se debe poder abandonar el ingreso, si el usuario en lugar de ingresar una
letra, ingresa el valor “0”, ó la palabra “FIN”.
Se debe validar que el ingreso sea una letra, cualquier otro caracter o una mayor
cantidad de letras, debe ser no tenido en cuenta, advirtiendo el hecho, con el
mensaje “Ingreso Inválido”, y se debe volver a solicitar una letra.
Para poder probar esta etapa, simplemente utiliza una palabra a adivinar que se
pueda establecer fácilmente, es recomendable pasar la palabra en cuestión, a través
de un parámetro.
Etapa 2 - Construcción de un Diccionario de Palabras candidatas
Ahora el objetivo será generar un diccionario de palabras candidatas a adivinar.
Se les proveerá de una función que devolverá un texto del cual extraerán las
palabras para formar el diccionario. El texto debe ser procesado, de forma tal de
obtener palabras que sólo estén formadas por letras, y no deben repetirse, y como
mínimo tener 5 letras.
Asociado a cada palabra, se debe guardar la cantidad de veces que la misma
aparecía en el texto. 


Una vez generado el diccionario de palabras, se debe mostrar por pantalla el
resultado, ordenado alfabéticamente; e informar el total de palabras que hay en el
diccionario.
Prueba lo realizado en esta etapa, controla que tu generación de palabras sea
correcta.
Etapa 3 - Elección de palabra candidata a Adivinar por el Jugador
Ahora que tenemos nuestro diccionario, podremos utilizarlo para obtener una palabra
candidata a adivinar.
Escribí una función, que reciba como primer parámetro el diccionario, y un segundo
parámetro opcional, con la longitud de la palabra a obtener. La función deberá
devolver aleatoriamente una palabra entre todas las posibles, teniendo en cuenta
que si fue pasada, debe tener la longitud indicada. Si el parámetro de longitud no es
provisto, entonces, todas las palabras participan de la elección.
Ten en cuenta que, si la longitud es provista, lo que debes hacer primero es generar
un conjunto de todas las palabras con dicha longitud, y entonces, recién sobre este
grupo, elegir una de forma aleatoria, utilizando la librería correspondiente.
Para probar tu función, utiliza un ciclo que la invoque al menos 100 veces, y analiza
lo que obtienes como palabra a adivinar. Repite el proceso varias veces.
Además de la función principal de esta etapa, puedes escribir todas las que
consideres necesarias, teniendo en cuenta los conceptos aprendidos en clase sobre
programación estructurada y programación modular.
Etapa 4 - Integración
En esta etapa debemos integrar las funcionalidades resueltas en cada una de las
etapas anteriores, haciendo un uso adecuado de las funciones escritas.
La secuencia del juego debe ser la siguiente:
1. Se deberá comenzar con la generación del diccionario de palabras.
2. Luego se debe solicitar al jugador, que ingrese la longitud de la palabra que desea
adivinar, validando dicho ingreso. En caso de no ingresar ningún valor, todas las
palabras serán candidatas; sino sólo aquellas que cumplan con dicha longitud.
3. El programa elegirá al azar una palabra a adivinar por el jugador.
4. Elegida la palabra, mostrará tantos signos de pregunta como letras compongan la
palabra elegida, y a continuación le pedirá al jugador que ingrese una letra,
implementando así, lo realizado en la etapa 3. 

Etapa 5 - Puntaje
Hasta ahora nuestro jugador, simplemente gana o pierde.
En esta etapa vamos a permitir que obtenga puntaje y que el mismo se acumule de
partida tras partida.
Si la letra elegida por el jugador se encuentra en la palabra, obtendrá 10 puntos por
haber acertado, de lo contrario, se le restarán 5 puntos. El puntaje final obtenido
podrá ser negativo.
Al finalizar una partida, se le ofrecerá si desea jugar otra; así hasta que responda
que no. El puntaje obtenido en la última partida, se tomará como inicio de la
siguiente. Al inicio de la ejecución del 1er. juego, el puntaje se encuentra en cero.
Condiciones de Entrega
Las siguientes condiciones deben ser respetadas para que la entrega sea considerada
válida:
1. Cada función que forma parte del código debe tener debajo de su firma, una
descripción corta de cuál es su objetivo y quien es el autor ó responsable de
dicha función.
2. El código correspondiente a la Parte 1, debe ser subido al campus. El nombre a
dar al archivo será TP1_NombreGrupo.py. Deberán reemplazar NombreGrupo,
por el nombre dado a su grupo. Si la entrega está compuesta por más de un
archivo .py, generar un .zip con todos los archivos .py, y nombrarlo de igual
modo, pero con extensión zip.
3. Deberán grabar 2 videos y subirlos a un canal de Youtube, ó a Google Drive.
El primer video, cada integrante del equipo, deberá contar mostrando el código,
qué parte estuvo bajo su responsabilidad y los puntos de solución dados, que
considere más relevantes. El video total no debe superar los 10 minutos.
Comenzar cada uno de los relatos, diciendo el nombre y apellido.
4. Deberán grabar un segundo video, en el que se muestre al menos una jugada
completa, y que contemple distintos casos que muestran que la aplicación
responde según lo esperado. Deberán ir relatando los eventos de la jugada. En
este caso el video puede estar realizado por 1 único integrante. 
