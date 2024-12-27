# Sokoban

## Descripción
Sokoban es un juego de lógica en el que el jugador debe empujar cajas para colocarlas en una posición determinada marcada en el mapa. El jugador puede moverse en las cuatro direcciones cardinales, pero no puede atravesar paredes ni cajas. Tampoco se puede empujar dos cajas a la vez. El juego termina cuando todas las cajas están en su posición final.

Esta implementación permite deshacer movimientos utilizando la tecla "p" y reiniciar el nivel con la tecla "r". 

En caso de que el jugador no encuentre una solución, puede pedir una pista con la tecla "h". Se buscará una solución al problema
usando Backtracking. Si no se encuentra una solución, se mostrará un mensaje indicando que no se encontró una solución. Si encuentra solución, se mostrará un mensaje indicando que se encontró una solución y si se sigue presionando la tecla "h", el nivel se resolverá automáticamente.

## Pasos para ejecutar el juego

1. Clonar el repositorio
2. Instalar las dependencias con el comando 
```py
sudo apt-get install python3-tk
```

3. Ejecutar el archivo `main.py` con el comando 
```py
python3 main.py
```