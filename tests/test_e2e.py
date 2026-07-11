import subprocess

def test_app_e2e():
    resultado = subprocess.run(
        ["python", "app.py"],
        capture_output=True,
        text=True
    )
    
    assert "Bienvenido a la calculadora" in resultado.stdout
    assert "El resultado de la suma es: 5" in resultado.stdout
    assert "Resultado obtenido de la base de datos: 5" in resultado.stdout
    assert "Final de la ejecución del flujo" in resultado.stdout