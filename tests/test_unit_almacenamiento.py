from src.almacenamiento import *

def test_guardar():
    db.clear()
    guardar_datos("suma_1", 5)
    assert 'suma_1' in db
    assert db['suma_1'] == 5

def test_obtener():
    db.clear()
    guardar_datos("suma_1", 5)
    resultado = obtener_datos("suma_1")
    assert resultado == 5