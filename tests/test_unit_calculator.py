from src.calculator import *

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(5, 3) == 2
    assert resta(0, 0) == 0
    assert resta(-1, -1) == 0

def test_division():
    assert division(6, 3) == 2
    assert division(1, 0) == "Error: División por cerro no está definido"