from src.calculator import *
from src.almacenamiento import *

def test_opracion_almacenamiento():
    resultado_suma = suma(2, 3)
    guardar_datos("suma_2_3", resultado_suma)
    dato_recuperado = obtener_datos("suma_2_3")
    assert dato_recuperado == 5