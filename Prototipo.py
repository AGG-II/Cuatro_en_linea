def tableroVacio():
    return [
            [0, 0, 0, 0, 0, 0, 0],        
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],        
    ]

def completarTableroEnOrden(secuencia, tablero):
    ficha = 1
    for i in secuencia:
        soltarFichaEnColumna(ficha, i, tablero)
        if ficha == 2:
            ficha = 1
        else:
            ficha = 2
    return tablero

def soltarFichaEnColumna(ficha, columna, tablero):
    for fila in  range(6, 0, -1):
        if tablero[fila - 1][columna - 1] == 0:
            tablero[fila - 1][columna - 1] = ficha
            return tablero

def dibujarTablero(tablero):
    for x in tablero:
        print(x)

secuencia = [1, 2, 3, 1]
dibujarTablero(
    completarTableroEnOrden(
        secuencia, tableroVacio()
        )
    )