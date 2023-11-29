import psutil

def obtener_datos_red():
    # Obtener el número total de bytes recibidos y transmitidos
    bytes_recibidos = psutil.net_io_counters().bytes_recv
    bytes_transmitidos = psutil.net_io_counters().bytes_sent

    return bytes_recibidos, bytes_transmitidos

# Mostrar el número total de bytes recibidos y transmitidos
bytes_recibidos, bytes_transmitidos = obtener_datos_red()
print("El número total de bytes recibidos es:", bytes_recibidos)
print("El número total de bytes transmitidos es:", bytes_transmitidos)