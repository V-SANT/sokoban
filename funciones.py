import soko
import gamelib
import pila

#ARCHIVOS
ARCHIVO_NIVELES = "niveles.txt"
ARCHIVO_TECLAS = "teclas.txt"

#ACCIONES
acciones = [soko.NORTE,soko.SUR,soko.ESTE,soko.OESTE]

#DATOS
def cargar_niveles():
    '''Abre el archivo niveles.txt y devuelve una lista con todas las descripciones de los niveles disponibles'''
    desc = []
    Niveles =[]
    
    with open(ARCHIVO_NIVELES) as niveles:
        for linea in niveles:
            if linea.rstrip("\n") == '':
                if soko.PARED not in desc[1]:
                    desc.pop(1)
                Niveles.append(desc)
                desc = []
            else:
                desc.append(linea.rstrip("\n"))        
    
    return Niveles

def cargar_teclas():
    '''Abre el archivo teclas.txt y devuelve un diccionario con las teclas como claves y las acciones como valores.'''
    
    controles = {}

    with open(ARCHIVO_TECLAS) as archivo_t:
        for linea in archivo_t:   
            tecla , accion = (linea.rstrip("\n")).split(" = ")
            controles[tecla] = soko.mapear(accion) 
    
    return controles

#GRAFICOS
def dibujar_nivel(grilla,nombre):
    '''Recibe la grilla y el nombre de un nivel y lo dibuja usando las funciones de gamelib'''

    Tamaño_Columna , Tamaño_Fila = soko.dimensiones(grilla)
    gamelib.resize(64*Tamaño_Columna, 64*Tamaño_Fila + 64)
    
    gamelib.draw_text(nombre,Tamaño_Columna*64/2, 64*Tamaño_Fila + 32, size=25, fill = "yellow")

    for x in range(0,Tamaño_Fila):
        for y in range(0,Tamaño_Columna):
            gamelib.draw_image('img/ground.gif', y*64, x*64)
        
    for x,fila in enumerate(grilla):
        for y in range(0,len(fila)):
            if soko.hay_caja(grilla,y,x):
                gamelib.draw_image('img/box.gif', y*64, x*64)
            if soko.hay_pared(grilla,y,x):
                gamelib.draw_image('img/wall.gif', y*64, x*64)
            if soko.hay_jugador(grilla,y,x):
                gamelib.draw_image('img/player.gif', y*64, x*64)
            if soko.hay_objetivo(grilla,y,x):
                gamelib.draw_image('img/goal.gif', y*64, x*64)

#SOKO
pila_estados = pila.Pila()
pila_pistas = pila.Pila()

def apilar_estados(grilla):
    "Guarda los movimientos realizados por el usuario en la pila de estados"
    pila_estados.apilar(grilla)

def desapilar_estados(nivel):
    '''Devuelve el estado que se encuentra en el tope de la pila, es decir el último que se realizó.
        Recibe el nivel como parámetro para devolver el estado inicial en caso de que la pila esté vacía'''
    if pila_estados.esta_vacia():
        return soko.crear_grilla(nivel)
    return pila_estados.desapilar()

def h(grilla):
    "Convierte la estructura de datos en una inmutable para facilitar su comparación"
    cadena = ""
    for f in grilla:
        for c in f:
            cadena += c
    return tuple(cadena)

def backtrack(grilla,visitados):
    """Recorre recursivamente los estados del juego. Devuelve un tupla con un Booleano y una pila con la solucion
    del nivel en caso de que la encuentre. Sino, devuelve None"""
    
    visitados[h(grilla)] = grilla 
    if soko.juego_ganado(grilla):
        #Solución Encontrada ---> Caso Base
        pistas = pila_pistas
        return True,pistas
    for accion in acciones:
        nueva_grilla = soko.mover(grilla,accion)
        if h(nueva_grilla) in visitados:
            continue
        solucion_encontrada,pistas = backtrack(nueva_grilla,visitados)
        if solucion_encontrada:
            pistas.apilar(accion)
            return True,pistas
    return False,None
        
def buscar_solucion(grilla_inicial):
    """Activa la funcion Backtrack para devolver una pila con la solución"""
    visitados = {}
    return backtrack(grilla_inicial,visitados)