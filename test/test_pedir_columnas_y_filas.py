from src.Prototipo import contenidoColumna
from src.Prototipo import contenidoFila

def test_contenido_correcto():
    tablero = [
            [0, 0, 1, 0, 0, 0, 0],        
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 2, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0],
            [2, 2, 1, 2, 2, 2, 1],        
    ]
    assert [1,2,2,1,1,1] == contenidoColumna(3, tablero)
    assert [2,2,1,2,2,2,1] == contenidoFila(6, tablero)
