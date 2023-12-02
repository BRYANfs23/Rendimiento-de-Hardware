import psutil
import platform
import os
import platform
import wmi        #Implementacion de las nuevas librerias que necesitaremos
import socket

# Uso del CPU
def obtener_informacion_cpu():

    
    uso_cpu = psutil.cpu_percent(interval=1)
    # Frecuencia del CPU
    frecuencia_cpu = psutil.cpu_freq()

    print(f"Uso del CPU: {uso_cpu}%")
    print(f"Frecuencia del CPU: {frecuencia_cpu.current} MHz")

def obtener_informacion_memoria():
    # Uso de la memoria
    uso_memoria = psutil.virtual_memory()

    print(f"Uso de la memoria: {uso_memoria.percent}%")

def obtener_informacion_red():
    # Estadísticas de red
    estadisticas_red = psutil.net_io_counters()

    print(f"Bytes enviados: {estadisticas_red.bytes_sent}")
    print(f"Bytes recibidos: {estadisticas_red.bytes_recv}")

#def obtener_temperatura_cpu():
#    sistema = platform.system()

#    if sistema == "Windows":
#        # Comando para obtener la temperatura en Windows
#        temperatura = os.popen("wmic /namespace:\\\\root\\cimv2 path Win32_TemperatureProbe get CurrentTemperature").read()
#        print(f"Temperatura del CPU: {temperatura.strip()} degrees Celsius")
#    elif sistema == "Linux" or sistema == "Darwin":
#        # Comando para obtener la temperatura en sistemas basados en Unix
#        temperatura = os.popen("sensors | grep 'Core 0'").read()
#        print(f"Temperatura del CPU: {temperatura.strip()}")

def obtener_temperatura_cpu():
    w = wmi.WMI(namespace="root/OpenHardwareMonitor")
    temperature_info = w.Sensor()

    for sensor in temperature_info:
        if "Temperature" in sensor.Name and "CPU Core" in sensor.Parent:
            print(f"Temperatura del CPU: {sensor.Value}°C")

def obtener_informacion_remota(ip, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, puerto))
        s.sendall(b'obtener_informacion')
        data = s.recv(1024).decode('utf-8')
        print(data)

def main():
    obtener_informacion_cpu()
    obtener_informacion_memoria()
    obtener_informacion_red()
    obtener_temperatura_cpu()

     # Por favor Colocar las direcciones IP de las computadoras que decea interconectar al sistema
     
    ip_computadora_1 = '192.168.1.101'
    ip_computadora_2 = '192.168.1.102'
    puerto = 12345  # Definicion de un puerto arbitrario para la comunicación

    print("\nInformación de la Computadora 1:")
    obtener_informacion_remota(ip_computadora_1, puerto)

    print("\nInformación de la Computadora 2:")
    obtener_informacion_remota(ip_computadora_2, puerto)

if __name__ == "__main__":
    main()
