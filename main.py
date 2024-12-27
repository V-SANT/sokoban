import soko
import gamelib
import funciones

#MENSAJES 
MENSAJE_1 = "Pensando..." #---> Gráficos
MENSAJE_2 = "Pista Disponible" #---> Gráficos
MENSAJE_3 = "Pista no Disponible" #---> Gráficos

def main():
    '''Gestiona los tres módulos para ejecutar el juego. Estos son:
        
        *Datos: Se encarga de abrir los archivos y convertirlos en estructuras a gestionar.
        *Graficos: Se encarga de dibujar la pantalla utilizando las funciones de gamelib.
        *soko: Es la estructura de datos del juego en sí. En ésta implementación es una lista de listas
        Además incluye otras estructuras auxiliares para ciertas funciones del juego''' 
    
    #Inicia el estado de juego 
    
    niveles = funciones.cargar_niveles() #---> Datos
    controles = funciones.cargar_teclas() #---> Datos
    mensaje = False #---> Gráficos

    contador_nivel = 0
    nivel = niveles[contador_nivel]
    nombre_nivel = nivel.pop(0)
    grilla = soko.crear_grilla(nivel)    
    
    while gamelib.is_alive():
        
        #Dibuja la pantalla con las imágenes en la carpeta img ---> Gráficos
        
        gamelib.draw_begin()
        if mensaje:
            funciones.dibujar_nivel(grilla,mensaje)
        else:
            funciones.dibujar_nivel(grilla,nombre_nivel)
        gamelib.draw_end()        
        
        #Actualiza el estado del juego según la tecla presionada
        
        ev = gamelib.wait(gamelib.EventType.KeyPress)
        tecla = ev.key
        
        if ev and tecla in controles:
            
            if controles[tecla] != "PISTAS":
                mensaje = False

            if controles[tecla] == soko.REINICIAR:
                grilla = soko.crear_grilla(niveles[contador_nivel])
                funciones.pila_estados.vaciar()
                funciones.pila_pistas.vaciar()

            elif controles[tecla] == "SALIR":
                break
            
            elif controles[tecla] == "DESHACER":
                funciones.pila_pistas.vaciar()
                grilla = funciones.desapilar_estados(nivel)
            
            elif controles[tecla] == "PISTAS":            
                
                if not mensaje:
                    mensaje = MENSAJE_1
                    gamelib.draw_begin()
                    funciones.dibujar_nivel(grilla,mensaje)
                    gamelib.draw_end()

                    try:
                        pista_disponible,pila_pistas= funciones.buscar_solucion(grilla)
                
                        if pista_disponible:
                            mensaje = MENSAJE_2
                        else:
                            mensaje = MENSAJE_3
                    
                    except RecursionError:
                        mensaje = MENSAJE_3
                        pila_pistas = None

                else:
                    if pila_pistas:
                        funciones.apilar_estados(grilla)
                        grilla = soko.mover(grilla,pila_pistas.desapilar())

            else:
                funciones.apilar_estados(grilla)
                funciones.pila_pistas.vaciar()
                grilla = soko.mover(grilla,controles[tecla])
    
        if ev and soko.juego_ganado(grilla):
            contador_nivel += 1
            nivel = niveles[contador_nivel]
            nombre_nivel = nivel.pop(0)
            grilla = soko.crear_grilla(nivel)
            funciones.pila_estados.vaciar()
            funciones.pila_pistas.vaciar()
            mensaje = False
        
        if not ev:
            break
    
gamelib.init(main)