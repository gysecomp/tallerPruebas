from src.calculator import *
from src.almacenamiento import *

def ejecuar_flujo():
    print("Bienvenido a la calculadora")

    resultado = suma(2,3)
    print(f"El resultado de la suma es: {resultado}")
    guardar_datos("suma_2_3", resultado)
    obtenido = obtener_datos("suma_2_3")
    print(f"Resultado obtenido de la base de datos: {obtenido}")
    print("Final de la ejecución del flujo")

if __name__ == "__main__":
    ejecuar_flujo()