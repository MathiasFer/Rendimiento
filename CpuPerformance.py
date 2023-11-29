import psutil

def obtener_uso_cpu():
    # Obtener el porcentaje de uso de la CPU
    porcentaje_uso = psutil.cpu_percent()

    return porcentaje_uso

# Mostrar el porcentaje de uso de la CPU
print("El uso de la CPU es:", obtener_uso_cpu(), "%")