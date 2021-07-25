def tableroVacio():
    return [
            [0, 0, 0, 0, 0, 0, 0],        
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],        
    ]

def contenidoColumna(nro_columna, tablero):
    columna = []
    for fila in tablero:
        celda = fila[nro_columna - 1]
        columna.append(celda)
    return columna

def contenidoFila(nro_fila, tablero):
    return tablero[nro_fila - 1]

def devolverColumnas(tablero):
    columnas = []
    for i in range(1, 8, 1):
        columnas.append(contenidoColumna(i, tablero))
    return columnas

def devolverFilas(tablero):
    return tablero

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
    if columna >= 1 and columna <= 7:
        for fila in  range(6, 0, -1):
            if tablero[fila - 1][columna - 1] == 0:
                tablero[fila - 1][columna - 1] = ficha
                return tablero
    else:
        print("Movimiento invalido, la columna ", columna ,"no existe.")        

def dibujarTablero(tablero):
    for x in tablero:
        print("|    ", end = '')
        for y in x:
            print(y, "  ", end = '')
        print("|")
    print("+--------------------------------+")

secuencia = [1, 2, 3, 1, 2, 3]
dibujarTablero(
    completarTableroEnOrden(
        secuencia, tableroVacio()
        )
    )