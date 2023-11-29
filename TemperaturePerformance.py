import psutil

def obtener_temperatura_cpu():
    # Obtener la temperatura actual de la CPU
    temperatura = psutil.sensors_temperatures()['cpu_thermal'][0].current

    return temperatura

# Mostrar la temperatura actual de la CPU
temperatura = obtener_temperatura_cpu()
print("La temperatura actual de la CPU es:", temperatura, "grados Celsius")