from src.Prototipo import completarTableroEnOrden
from src.Prototipo import soltarFichaEnColumna
from src.Prototipo import tableroVacio

def test_coloca_correctamente():
    tablero1 = tableroVacio()
    tablero2 = tableroVacio()
    secuencia = [1, 2, 3, 1, 2, 3]

    assert [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0],] == soltarFichaEnColumna(1, 1, tablero2)
    assert [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 2, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0],] == completarTableroEnOrden(secuencia,tablero1)