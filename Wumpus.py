import sys
import pygame
from pygame.locals import KEYDOWN, K_q
from collections import deque
import numpy as np
import time

# CONSTANTES:
SCREENSIZE = WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
GOLD = (252, 244, 25)
GREY = (160, 160, 160)
RED= (255, 0, 0)

cazador = []
mounstro = [-1,-1]
pozo_uno = [-1,-1]
pozo_dos = [-1,-1]
oro = [-1,-1]
camino = []
RNG = True
# Array que sera el mapa:
#cellMAP = np.random.randint(2, size=(10, 10))
#cellMAP = np.zeros((10, 10), dtype=int)
grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
cellMAP = np.array(grid)#Colocacion de elementos de forma aleatoria:
listaX = np.random.permutation(10)[:4]
listaY = np.random.permutation(10)[:4]
for i in range(3):
    if(listaX[i]==0 and listaY[i]==0):
        RNG=False
        listaX = np.random.permutation(10)[:4]
        listaY = np.random.permutation(10)[:4]
        print("Posicion imposible evadida")
    elif(listaX[i]==0 and listaY[i]==1):
        RNG=False
        listaX = np.random.permutation(10)[:4]
        listaY = np.random.permutation(10)[:4]
        print("Posicion imposible evadida")
    elif(listaX[i]==1 and listaY[i]==0):
        RNG=False
        listaX = np.random.permutation(10)[:4]
        listaY = np.random.permutation(10)[:4]
        print("Posicion imposible evadida")
    else:
        RNG=True
while (RNG == True):
    cellMAP[0][0] = 1
    cellMAP[listaX[0]][listaY[0]] = 2
    cellMAP[listaX[1]][listaY[1]] = 3
    cellMAP[listaX[2]][listaY[2]] = 7
    cellMAP[listaX[3]][listaY[3]] = 4
    break   #print(grid)    cazador.append(0)
cazador.append(0)
cazador.append(0)    


def inicializador():
    #Colocacion de elementos de forma aleatoria:
    #cellMAP = np.array(grid)
    listaX = np.random.permutation(10)[:4]
    listaY = np.random.permutation(10)[:4]
    for i in range(3):
        if(listaX[i]==0 and listaY[i]==0):
            RNG=False
            listaX = np.random.permutation(10)[:4]
            listaY = np.random.permutation(10)[:4]
            print("Posicion imposible evadida")
        elif(listaX[i]==0 and listaY[i]==1):
            RNG=False
            listaX = np.random.permutation(10)[:4]
            listaY = np.random.permutation(10)[:4]
            print("Posicion imposible evadida")
        elif(listaX[i]==1 and listaY[i]==0):
            RNG=False
            listaX = np.random.permutation(10)[:4]
            listaY = np.random.permutation(10)[:4]
            print("Posicion imposible evadida")
        else:
            RNG=True

    while (RNG == True):
        cellMAP[0][0] = 1
        cellMAP[mounstro[1]][mounstro[0]] = 0
        cellMAP[pozo_uno[1]][pozo_uno[0]] = 0
        cellMAP[pozo_dos[1]][pozo_dos[0]] = 0
        cellMAP[oro[1]][oro[0]] = 0
        '''
        cellMAP[listaX[0]][listaY[0]] = 2
        cellMAP[listaX[1]][listaY[1]] = 3
        cellMAP[listaX[2]][listaY[2]] = 7
        cellMAP[listaX[3]][listaY[3]] = 4
        '''
        mounstro[0] = listaX[0]
        mounstro[1] = listaY[0]
        pozo_uno[0] = listaX[1]
        pozo_uno[1] = listaY[1]
        pozo_dos[0] = listaX[2]
        pozo_dos[1] = listaY[2]
        oro[0] = listaX[3]
        oro[1] = listaY[3]
        
        reposicionar()
        break

    #print(grid)    

    cazador[0]=0
    cazador[1]=0    

#Variables:
_VARS = {'surf': False, 'gridWH': 400,
         'gridOrigin': (200, 100), 'gridCells': cellMAP.shape[0], 'lineWidth': 2}

#Inicializar el programa
def main():
    pygame.init()
    _VARS['surf'] = pygame.display.set_mode(SCREENSIZE)
    while True:
        checkEvents()
        _VARS['surf'].fill(GREY)
        drawSquareGrid(
         _VARS['gridOrigin'], _VARS['gridWH'], _VARS['gridCells'])
        placeCells()
        reposicionar()
        drawCazador()
        pygame.display.update()

# Añadir celdas :
def placeCells():
    # Dimensiones de las celdas
    cellBorder = 6
    celldimX = celldimY = (_VARS['gridWH']/_VARS['gridCells']) - (cellBorder*2)
    # Rellenar
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            # La celda contiene un elemento?
            """
            0 = Casilla vacia
            1 = Cazador
            2 = Mounstro
            3 = Pozo 1 y 2
            4 = Oro
            5 = Mal Olor
            6 = Brisa
            """
            
            if(cellMAP[column][row] == 2):
                wumpus = pygame.image.load("wumpus.png").convert_alpha()
                _VARS['surf'].blit(wumpus, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)

                mounstro[0] = row
                mounstro[1] = column
            if(cellMAP[column][row] == 3):

                pozo = pygame.image.load("pozo.png").convert_alpha()
                _VARS['surf'].blit(pozo, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
                pozo_uno[0] =row
                pozo_uno[1] =column
            if(cellMAP[column][row] == 4):
                gold = pygame.image.load("gold.png").convert_alpha()
                _VARS['surf'].blit(gold, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
                oro[0] =row
                oro[1] =column
            if(cellMAP[column][row] == 5):
                olor = pygame.image.load("olor.png").convert_alpha()
                _VARS['surf'].blit(olor, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
            if(cellMAP[column][row] == 6):
                brisa = pygame.image.load("brisa.png").convert_alpha()
                _VARS['surf'].blit(brisa, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
            elif(cellMAP[column][row] == 7):
                pozo2 = pygame.image.load("pozo.png").convert_alpha()
                _VARS['surf'].blit(pozo2, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
                pozo_dos[0] =row
                pozo_dos[1] =column
            
            elif(cellMAP[column][row] == 10):
                drawSquareCell(
                        _VARS['gridOrigin'][0] + (celldimY*row)
                        + cellBorder + (2*row*cellBorder) + _VARS['lineWidth']/2,
                        _VARS['gridOrigin'][1] + (celldimX*column)
                        + cellBorder + (2*column*cellBorder) + _VARS['lineWidth']/2,
                        celldimX, celldimY, RED)
            '''    
                #DIBUJAR SPRITE
                spk = pygame.image.load("spelunker.png").convert_alpha()
                _VARS['surf'].blit(spk, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)
                #--------------
                '''                

# Dibujar los cuadrados
def drawSquareCell(x, y, dimX, dimY, Color):
    pygame.draw.rect(
     _VARS['surf'], Color,
     (x, y, dimX, dimY)
    )

def drawCazador():
    # Dimensiones de las celdas
    cellBorder = 6
    celldimX = celldimY = (_VARS['gridWH']/_VARS['gridCells']) - (cellBorder*2)
    # Rellenar
    for row in range(cellMAP.shape[0]):
        for column in range(cellMAP.shape[1]):
            if(cellMAP[column][row] == 1):
                spk = pygame.image.load("spelunker.png").convert_alpha()
                _VARS['surf'].blit(spk, (_VARS['gridOrigin'][0] + (celldimY*row)
                    +(2*row*cellBorder) + _VARS['lineWidth']/2,_VARS['gridOrigin'][1] + (celldimX*column)
                    +(2*column*cellBorder) + _VARS['lineWidth']/2),)


#CONTROLADOR DE MOVIMIENTO

def movimiento(direccion):
    if (direccion=="abajo"):
        if cazador[1]<9:
            cellMAP[cazador[1]][cazador[0]]=0
            cellMAP[cazador[1]+1][cazador[0]]=1
            cazador[1] = cazador[1]+1
    elif (direccion=="arriba"):
        if  cazador[1]>0:
            cellMAP[cazador[1]][cazador[0]]=0
            cellMAP[cazador[1]-1][cazador[0]]=1
            cazador[1] = cazador[1]-1
    elif (direccion=="izquierda"):
        if cazador[0]>0:
            cellMAP[cazador[1]][cazador[0]]=0
            cellMAP[cazador[1]][cazador[0]-1]=1
            cazador[0] = cazador[0]-1
    elif (direccion=="derecha"):
        if cazador[0]<9:
            cellMAP[cazador[1]][cazador[0]]=0
            cellMAP[cazador[1]][cazador[0]+1]=1
            cazador[0] = cazador[0]+1
    '''
    #CONDICION DE VICTORIA
    if (cazador[0]==oro[0] and cazador[1]==oro[1]):
        ctypes.windll.user32.MessageBoxW(0, "Has conseguido el oro!", "You win", 0)
        sys.exit()
    '''
    reposicionar()
#_________________________


def reposicionar():
    
    cellMAP[mounstro[1]][mounstro[0]]=2
    cellMAP[pozo_uno[1]][pozo_uno[0]]=3
    cellMAP[pozo_dos[1]][pozo_dos[0]]=7
    cellMAP[oro[1]][oro[0]]=4

    '''
    myFont = pygame.font.SysFont("Times New Roman", 18)
    randNumLabel = myFont.render("XD", 1, (0,0,0))
    _VARS['surf'].blit(randNumLabel, (520, 20))  
    '''
    #Dibujar brisa y mal olor
    #Pozo 1
    if pozo_uno[0]>0:    
        cellMAP[pozo_uno[1]][pozo_uno[0]-1] = 6                 
    if pozo_uno[0]<9:
        cellMAP[pozo_uno[1]][pozo_uno[0]+1] = 6
    if pozo_uno[1]<9:
        cellMAP[pozo_uno[1]+1][pozo_uno[0]] = 6
    if pozo_uno[1]>0:
        cellMAP[pozo_uno[1]-1][pozo_uno[0]] = 6
    #Pozo 2
    if pozo_dos[0]>0:
        cellMAP[pozo_dos[1]][pozo_dos[0]-1] = 6                       
    if pozo_dos[0]<9:
        cellMAP[pozo_dos[1]][pozo_dos[0]+1] = 6
    if pozo_dos[1]<9:
        cellMAP[pozo_dos[1]+1][pozo_dos[0]] = 6
    if pozo_dos[1]>0:
        cellMAP[pozo_dos[1]-1][pozo_dos[0]] = 6
    #Mounstro
    if mounstro[0]>0:
        cellMAP[mounstro[1]][mounstro[0]-1] = 5                       
    if mounstro[0]<9:
        cellMAP[mounstro[1]][mounstro[0]+1] = 5
    if mounstro[1]<9:
        cellMAP[mounstro[1]+1][mounstro[0]] = 5
    if mounstro[1]>0:
        cellMAP[mounstro[1]-1][mounstro[0]] = 5
    if(camino!=None):
        for x,y in camino:
            cellMAP[x][y] = 10
    cellMAP[cazador[1]][cazador[0]]=1   

def drawSquareGrid(origin, gridWH, cells):

    CONTAINER_WIDTH_HEIGHT = gridWH
    cont_x, cont_y = origin

    # Dibujar bordes:
    # Arriba de izquierda a derecha
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y), _VARS['lineWidth'])
    # Abajo de izquierda a derecha
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, CONTAINER_WIDTH_HEIGHT + cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x,
       CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])
    # # Izquierda de arriba hacia abajo
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (cont_x, cont_y),
      (cont_x, cont_y + CONTAINER_WIDTH_HEIGHT), _VARS['lineWidth'])
    # # Derecha de arriba hacia abajo
    pygame.draw.line(
      _VARS['surf'], BLACK,
      (CONTAINER_WIDTH_HEIGHT + cont_x, cont_y),
      (CONTAINER_WIDTH_HEIGHT + cont_x,
       CONTAINER_WIDTH_HEIGHT + cont_y), _VARS['lineWidth'])

    # Obtener el tamaño de las celdas
    cellSize = CONTAINER_WIDTH_HEIGHT/cells

    # DIVISIONES VERTICALES :
    for x in range(cells):
        pygame.draw.line(
           _VARS['surf'], BLACK,
           (cont_x + (cellSize * x), cont_y),
           (cont_x + (cellSize * x), CONTAINER_WIDTH_HEIGHT + cont_y), 2)
    # # DIVISIONES HORIZONTALES
        pygame.draw.line(
          _VARS['surf'], BLACK,
          (cont_x, cont_y + (cellSize*x)),
          (cont_x + CONTAINER_WIDTH_HEIGHT, cont_y + (cellSize*x)), 2)

def auxMov(direccion):
    pygame.time.Clock().tick(8)
    movimiento(direccion)
    _VARS['surf'].fill(GREY)
    drawSquareGrid(
         _VARS['gridOrigin'], _VARS['gridWH'], _VARS['gridCells'])
    placeCells()
    drawCazador()
    pygame.display.update()
    


def getNewPosition(position, direction):
    row, col = position
    if direction == 'left':
        col -= 1
    elif direction == 'right':
        col += 1
    elif direction == 'up':
        row -= 1
    elif direction == 'down':
        row += 1
    return (row, col)


def moves(row, col):
    valid_moves = []
    if row > 0:
        valid_moves.append('up')
    if row < 9:
        valid_moves.append('down')
    if col > 0:
        valid_moves.append('left')
    if col < 9:
        valid_moves.append('right')
    return valid_moves

# Encontrar la ruta hacia el oro
def find_path(start_row, start_col, end_row, end_col, path):
    # base case
    if start_row == end_row and start_col == end_col:
        return True

    # Marcar la posicion inicial como "Visitada"
    cellMAP[start_row][start_col] = 9

    # Verificar si el movimiento es valido
    valid_moves = moves(start_row, start_col)

    # Funcion para realizar movimientos
    for move in valid_moves:
        if move == 'up':
            new_row = start_row - 1
            new_col = start_col
        elif move == 'down':
            new_row = start_row + 1
            new_col = start_col
        elif move == 'left':
            new_row = start_row
            new_col = start_col - 1
        elif move == 'right':
            new_row = start_row
            new_col = start_col + 1

        # Probar si el movimiento es valido
        if cellMAP[new_row][new_col] not in [2, 3, 7, 9]:
            # Añadir el movimiento a la ruta y llamar a la función de forma recursiva
            path.append(move)
            if find_path(new_row, new_col, end_row, end_col, path):
                return True
            # Remover el movimiento de la ruta si no se llego a la meta
            path.pop()

    # Marcar la posicion actual como recorrida
    cellMAP[start_row][start_col] = 0

    # Regresar falso si el oro no fue encontrado
    return False


#FUNCION PARA IR DIRECTO AL ORO
def directPath(board, start, goal):
    visited = set([start])
    queue = deque([(start, [])])

    while queue:
        position, path = queue.popleft()
        if position == goal:
            return path
        for direction in ['left', 'right', 'up', 'down']:
            newPosition = getNewPosition(position, direction)
            if newPosition in visited:
                continue
            row, col = newPosition
            if row < 0 or row >= 10 or col < 0 or col >= 10:
                continue
            if board[row][col] == 0 or board[row][col] == 4 or board[row][col] == 5  or board[row][col] == 6:
                visited.add(newPosition)
                newPath = path + [direction]
                queue.append((newPosition, newPath))

    return []
#______________________________

def test():
    path = []
    find_path(cazador[0], cazador[1], oro[1], oro[0], path)
    #print(path)
    for mov in path:
        if mov=="up":
            auxMov("arriba")
        elif mov=="down":
            auxMov("abajo")
        elif mov=="left":
            auxMov("izquierda")
        elif mov=="right":
            auxMov("derecha")
    #regresar al inicio
    cellMAP[cazador[1]][cazador[0]]=0
    cellMAP[0][0]=1
    cazador[0]=0
    cazador[1]=0
    time.sleep(3)
    drawCazador()
    pygame.display.update()
    #ir directo al oro
    hunterPos = (cazador[1], cazador[0])
    goal = (oro[1], oro[0])
    directPathArr = directPath(cellMAP, hunterPos, goal)
    for mov in directPathArr:
        if mov=="up":
            items = (cazador[1],cazador[0])
            camino.append(items)
            cellMAP[cazador[1]][cazador[0]]=10
            auxMov("arriba")
        elif mov=="down":
            items = (cazador[1],cazador[0])
            camino.append(items)
            cellMAP[cazador[1]][cazador[0]]=10
            auxMov("abajo")
        elif mov=="left":
            items = (cazador[1],cazador[0])
            camino.append(items)
            cellMAP[cazador[1]][cazador[0]]=10
            auxMov("izquierda")
        elif mov=="right":
            items = (cazador[1],cazador[0])
            camino.append(items)
            cellMAP[cazador[1]][cazador[0]]=10
            auxMov("derecha")


def checkEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_DOWN:
                movimiento("abajo")
            elif event.key == pygame.K_UP:
                movimiento("arriba")
            elif event.key == pygame.K_LEFT:
                movimiento("izquierda")
            elif event.key == pygame.K_RIGHT:
                movimiento("derecha")
            elif event.key == pygame.K_s:
                test()
            elif event.key == pygame.K_n:
                cellMAP.fill(0)
                inicializador()
                cellMAP[cazador[1]][cazador[0]]=0
                cellMAP[0][0]=1
                cazador[0]=0
                cazador[1]=0
                camino.clear()
                for X in range(10):
                    for Y in range(10):
                        cellMAP[X-1][Y-1]=0
                placeCells()
                reposicionar()
                drawCazador()
                pygame.display.update()
            elif event.key == pygame.K_SPACE:
                for y in range(9):
                    auxMov("derecha")
                auxMov("abajo")
                switch = False
                for x in range(5):
                    if(switch==True):                   
                        for y in range(9):
                            auxMov("derecha")
                        switch=False
                        auxMov("abajo")
                    if(switch==False):                   
                        for y in range(9):
                            auxMov("izquierda")
                        switch=True
                        auxMov("abajo")
                for z in range(9):
                    auxMov("arriba")
if __name__ == '__main__':
        main()