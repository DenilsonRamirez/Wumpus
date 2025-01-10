# Wumpus hecho en PyGame
Buscador automatico del camino más simple hacia el "oro", unicamente se requiere de PyGame, numpy y time como dependencia.
![image](https://github.com/user-attachments/assets/a34589cd-218c-48fd-a2c2-de8b44eea92c)

## Funcionamiento
Se genera un tablero de 10x10 casillas y se posicionan de forma aleatoria los elementos en pantalla, 2 pozos con brisa y 1 mounstro con pestilencia, cada uno de estas trampas tiene una advertencia en las 4 dirección cardinales adyacentes.  
Por último, tenemos al cazador que recorrerá el tablero empezando siempre en la posición 0 en X y 0 en Y.
El objetivo principal es recorrer el tablero con el camino mas corto posible y sin llegar a tocar los pozos o el mounstro, para llegar al oro que es la meta.
Para comenzar únicamente se debe presionar la tecla “S” y el cazador comenzara a recorrer el tablero buscando la mejor ruta, cuando encuentre el oro, este regresara a su posición inicial y mostrara el camino mas corto hacia el oro.
Si se desea iniciar un nuevo juego, únicamente se debe presionar la tecla “N” y el tablero junto con sus elementos serán reiniciados y se generaran aleatoriamente cada vez que se requiera.
 
## Metodo de busqueda
La función principal para encontrar el mejor camino es el algoritmo A* el cual encuentra el camino más corto entre un punto inicial y un punto final en una cuadrícula. El algoritmo utiliza una función heurística, que es una estimación de la distancia entre el nodo actual y el nodo meta, para guiar la búsqueda del camino más corto.

En el código, se utiliza el algoritmo A* para encontrar el camino más corto desde la posición inicial del cazador hasta el oro evitando las trampas. El algoritmo funciona explorando las casillas vecinas, calculando el coste de ir a cada casilla y registrando el mejor camino encontrado hasta el momento. El algoritmo repite este proceso hasta que alcanza la meta o determina que no hay ningún camino válido hacia ella.

Una vez que el algoritmo ha encontrado el camino más corto, lo almacena en una matriz llamada pathArr. Esta sirve para trazar el camino del cazador desde la posición inicial hasta la posición de meta. Luego se utiliza una función para determinar la dirección del movimiento de una celda a otra del camino. Por último, la función devuelve la matriz pathArr, que puede utilizarse para mover al cazador desde la posición inicial hasta la posición de meta.
