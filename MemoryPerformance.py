import psutil

def obtener_uso_memoria():
    # Obtener el porcentaje de uso de la memoria
    porcentaje_uso = psutil.virtual_memory().percent

    return porcentaje_uso

# Mostrar el porcentaje de uso de la memoria
print("El uso de la memoria es:", obtener_uso_memoria(), "%")