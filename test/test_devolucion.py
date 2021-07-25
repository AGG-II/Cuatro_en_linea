from src.Prototipo import devolverColumnas
from src.Prototipo import devolverFilas

def test_devuelve_correctamente():
    tablero = [
            [0, 0, 1, 0, 0, 0, 0],        
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [2, 2, 1, 2, 2, 2, 1],        
    ]
    assert [ [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2], [1, 2, 2, 1, 1, 1], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 1],] == devolverColumnas(tablero)
    assert tablero == devolverFilas(tablero)