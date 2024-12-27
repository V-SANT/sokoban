#CARACTERES DEL JUEGO
PARED = "#"
CAJA = "$"
JUGADOR = "@"
OBJETIVO = "."
OBJETIVO_CAJA = "*"
OBJETIVO_JUGADOR = "+"    
ESPACIO = " "



#DIRECCIONES
NORTE = (0,-1)
SUR = (0,1)
ESTE = (1,0)
OESTE = (-1,0)
REINICIAR = (0,0) #Uso un movimiento nulo para volver a la posición inicial



def mapear(cadena):
    '''Recibe una cadena y devuelve la direccion/accion que le corresponde'''
    if cadena == "NORTE":
        return NORTE
    elif cadena == "ESTE":
        return ESTE
    elif cadena == "SUR":
        return SUR
    elif cadena == "OESTE":
        return OESTE
    elif cadena == "REINICIAR":
        return REINICIAR
    return cadena


def crear_grilla(desc):
    '''Crea una grilla a partir de la descripción del estado inicial.

    La descripción es una lista de cadenas, cada cadena representa una
    fila y cada caracter una celda. Los caracteres pueden ser los siguientes:

    Caracter  Contenido de la celda
    --------  ---------------------
           #  Pared
           $  Caja
           @  Jugador
           .  Objetivo
           *  Objetivo + Caja
           +  Objetivo + Jugador
    '''
    grilla = []
    for filas in desc:
        L = []
        for caracter in filas:
            L.append(caracter)
        grilla.append(L)
    return grilla



def dimensiones(grilla):
    '''Devuelve una tupla con la cantidad de columnas y filas de la grilla.'''
    L = []
    for filas in grilla:
        L.append(len(filas))
    return (max(L),len(grilla))


def hay_pared(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == PARED



def hay_objetivo(grilla, c, f):
    '''Devuelve True si hay un objetivo en la columna y fila (c, f).'''
    return grilla[f][c] == OBJETIVO or grilla[f][c] == OBJETIVO_CAJA or grilla[f][c] == OBJETIVO_JUGADOR



def hay_caja(grilla, c, f):
    '''Devuelve True si hay una caja en la columna y fila (c, f).'''
    return grilla[f][c] == CAJA or grilla[f][c] == OBJETIVO_CAJA



def hay_jugador(grilla, c, f):
    '''Devuelve True si el jugador está en la columna y fila (c, f).'''
    return grilla[f][c] == JUGADOR or grilla[f][c] == OBJETIVO_JUGADOR



def hay_espacio(grilla, c, f):
    '''Devuelve True si hay una pared en la columna y fila (c, f).'''
    return grilla[f][c] == ESPACIO



def juego_ganado(grilla):
    '''Devuelve True si el juego está ganado.'''
    for f in grilla:
        for c in f:       
            if c in (OBJETIVO,OBJETIVO_JUGADOR,CAJA):
               return False
    return True



def posicion_jugador(grilla):
    """Recibe una grilla y devuelve una tupla con la columna y la fila (en ese orden) en la que se encuentra el jugador (@)"""
    for f in grilla:
        for c in f:
            if c in (JUGADOR,OBJETIVO_JUGADOR):
                return (f.index(c),grilla.index(f))



def posicion_nueva(grilla,direccion):
    """Recibe una grilla y devuelve una tupla con la columna y la fila (en ese orden) en la que se encuentra un caracter segun la direccion elegida"""
    x,y = direccion
    a = posicion_jugador(grilla)[0] + x
    b = posicion_jugador(grilla)[1] + y
    return a,b



def mover(grilla, direccion):
    '''Mueve el jugador en la dirección indicada.

    La dirección es una tupla con el movimiento horizontal y vertical. Dado que
    no se permite el movimiento diagonal, la dirección puede ser una de cuatro
    posibilidades:

    direccion  significado
    ---------  -----------
    (-1, 0)    Oeste
    (1, 0)     Este
    (0, -1)    Norte
    (0, 1)     Sur

    La función debe devolver una grilla representando el estado siguiente al
    movimiento efectuado. La grilla recibida NO se modifica; es decir, en caso
    de que el movimiento sea válido, la función devuelve una nueva grilla.
    '''
    
    grilla_2 = []
    
    for elementos in grilla:
        L_2 = []
        for caracteres in elementos:
            L_2.append(caracteres)
        grilla_2.append(L_2)

    jc,jf = posicion_jugador(grilla_2)
    nc,nf = posicion_nueva(grilla_2,direccion)
    x,y = direccion

    if hay_pared(grilla_2, nc, nf) or hay_caja(grilla, nc, nf) and hay_caja(grilla, nc + x, nf + y) or hay_caja(grilla, nc, nf) and hay_pared(grilla, nc + x, nf + y):
        return grilla
    
    elif hay_espacio(grilla_2, nc, nf):
        if hay_objetivo(grilla_2, jc, jf):
            grilla_2[jf][jc] = OBJETIVO
            grilla_2[nf][nc] = JUGADOR
        else:
            grilla_2[jf][jc] = ESPACIO
            grilla_2[nf][nc] = JUGADOR

    elif hay_objetivo(grilla_2, nc, nf) and not hay_caja(grilla_2, nc, nf):
        if hay_objetivo(grilla,jc,jf):
            grilla_2[jf][jc] = OBJETIVO
            grilla_2[nf][nc] = OBJETIVO_JUGADOR 
        else:
            grilla_2[jf][jc] = ESPACIO
            grilla_2[nf][nc] = OBJETIVO_JUGADOR   


    elif hay_caja(grilla_2, nc, nf):
        
        if hay_espacio(grilla_2, nc + x, nf + y):
            
            if hay_objetivo(grilla_2, jc, jf) and hay_objetivo(grilla_2, nc, nf):
                grilla_2[jf][jc] = OBJETIVO
                grilla_2[nf][nc] = OBJETIVO_JUGADOR
                grilla_2[nf + y][nc + x] = CAJA
            
            elif hay_objetivo(grilla_2, jc, jf):
                grilla_2[jf][jc] = OBJETIVO
                grilla_2[nf][nc] = JUGADOR
                grilla_2[nf + y][nc + x] = CAJA
            
            elif hay_objetivo(grilla_2, nc, nf):
                grilla_2[jf][jc] = ESPACIO
                grilla_2[nf][nc] = OBJETIVO_JUGADOR
                grilla_2[nf + y][nc + x] = CAJA
            
            else:
                grilla_2[jf][jc] = ESPACIO
                grilla_2[nf][nc] = JUGADOR
                grilla_2[nf + y][nc + x] = CAJA 
        
        if hay_objetivo(grilla_2, nc + x, nf + y):
            
            if hay_objetivo(grilla_2, nc, nf) and hay_objetivo(grilla_2, jc, jf):
                grilla_2[jf][jc] = OBJETIVO
                grilla_2[nf][nc] = OBJETIVO_JUGADOR
                grilla_2[nf + y][nc + x] = OBJETIVO_CAJA
            
            elif hay_objetivo(grilla_2, nc, nf) and hay_objetivo(grilla_2, jc, jf):
                grilla_2[jf][jc] = OBJETIVO
                grilla_2[nf][nc] = OBJETIVO_JUGADOR
                grilla_2[nf + y][nc + x] = OBJETIVO_CAJA
            
            elif hay_objetivo(grilla_2, jc, jf):
                grilla_2[jf][jc] = OBJETIVO
                grilla_2[nf][nc] = JUGADOR
                grilla_2[nf + y][nc + x] = OBJETIVO_CAJA
            
            elif hay_objetivo(grilla_2, nc, nf):
                grilla_2[jf][jc] = ESPACIO
                grilla_2[nf][nc] = OBJETIVO_JUGADOR
                grilla_2[nf + y][nc + x] = OBJETIVO_CAJA
            
            else:
                grilla_2[jf][jc] = ESPACIO
                grilla_2[nf][nc] = JUGADOR
                grilla_2[nf + y][nc + x] = OBJETIVO_CAJA
    
    
    return grilla_2