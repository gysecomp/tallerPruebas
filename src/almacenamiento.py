db = {}

def guardar_datos(operacion, resultado):
    db[operacion] = resultado

def obtener_datos(operacion):
    return db.get(operacion, "No se encontraron resultados para la operación especificada.")