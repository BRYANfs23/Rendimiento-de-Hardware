import psutil
import platform
import os
import platform

def obtener_informacion_cpu():
    # Uso del CPU
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

def obtener_temperatura_cpu():
    sistema = platform.system()

    if sistema == "Windows":
        # Comando para obtener la temperatura en Windows
        temperatura = os.popen("wmic /namespace:\\\\root\\cimv2 path Win32_TemperatureProbe get CurrentTemperature").read()
        print(f"Temperatura del CPU: {temperatura.strip()} degrees Celsius")
    elif sistema == "Linux" or sistema == "Darwin":
        # Comando para obtener la temperatura en sistemas basados en Unix
        temperatura = os.popen("sensors | grep 'Core 0'").read()
        print(f"Temperatura del CPU: {temperatura.strip()}")

def main():
    obtener_informacion_cpu()
    obtener_informacion_memoria()
    obtener_informacion_red()
    obtener_temperatura_cpu()

if __name__ == "__main__":
    main()
