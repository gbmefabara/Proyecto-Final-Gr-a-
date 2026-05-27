"""
Módulo de arranque (boot.py) para ESP32.
Este archivo se ejecuta automáticamente al encender o reiniciar el microcontrolador.
Su propósito principal es establecer la conexión a la red Wi-Fi local para
permitir el acceso al servidor web que controla la grúa.
Incluye un menú interactivo en terminal para detener el arranque y permitir
la programación/modificación de archivos (REPL libre).
"""
# boot.py
import network
import time
import sys
import uselect

# --- CONFIGURACIÓN DE WI-FI ---
# Los estudiantes pueden cambiar estas credenciales por las de su propia red o del colegio.
SSID = "TU_RED_WIFI"  # Cambia esto por el nombre de tu red Wi-Fi
PASSWORD = "TU_CLAVE_WIFI"  # Cambia esto por la contraseña de tu red Wi-Fi


def menu_inicio(timeout_segundos=5):
    """
    Muestra un menú en la terminal. Avanza automáticamente a ejecución si no hay respuesta.
    Permite detener el inicio automático para liberar la consola REPL.
    """
    print("\n" + "="*40)
    print("      SISTEMA DE CONTROL - GRÚA TORRE")
    print("="*40)
    print("1. Iniciar sistema normalmente (Modo Ejecución)")
    print("2. Detener en modo programación (Liberar REPL)")
    print(f"Selecciona una opción (Avanza a opción 1 en {timeout_segundos}s)...")

    poller = uselect.poll()
    poller.register(sys.stdin, uselect.POLLIN)

    tiempo_inicio = time.time()
    while (time.time() - tiempo_inicio) < timeout_segundos:
        if poller.poll(100):
            caracter = sys.stdin.read(1)
            if caracter == '1':
                print("\n-> Opción 1 seleccionada. Iniciando...")
                return True
            elif caracter == '2':
                print("\n-> Opción 2 seleccionada. Modo programación activo.")
                print("Consola REPL liberada. Puedes subir o modificar archivos.")
                return False

    print("\n-> Tiempo de espera agotado. Iniciando de forma automática...")
    return True


def connect_wifi(ssid=SSID, password=PASSWORD):
    """
    Función para conectar el ESP32 a la red Wi-Fi.
    """
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        print('Conectando a la red:', ssid)

        max_attempts = 5
        connected = False

        for attempt in range(1, max_attempts + 1):
            try:
                wlan.connect(ssid, password)
            except OSError as e:
                print('OSError en wlan.connect():', e)
                try:
                    print('Estado WLAN (wlan.status):', wlan.status())
                except Exception:
                    pass

            wait_start = time.time()
            while (time.time() - wait_start) < 5:
                if wlan.isconnected():
                    connected = True
                    break
                time.sleep(0.5)
                print('.', end='')

            if connected:
                break
            else:
                print('\nIntento', attempt, 'fallido. Reintentando...')

        if not connected:
            print('\nNo se pudo conectar en modo STA tras', max_attempts, 'intentos.')
            try:
                nets = wlan.scan()
                print('Redes detectadas (SSID, RSSI, Authmode):')
                for n in nets:
                    ss = n[0].decode('utf-8', 'ignore') if isinstance(n[0], (bytes, bytearray)) else str(n[0])
                    rssi = n[3]
                    auth = n[4]
                    print('-', ss, rssi, auth)
            except Exception as e:
                print('No se pudo realizar scan():', e)

            print('No se habilitará modo AP. Verifica las credenciales o el alcance de la red Wi-Fi.')
            return

    print('\n¡Conexión exitosa al Wi-Fi!')
    print('Ingresa esta Dirección IP en tu navegador para ver los controles:', wlan.ifconfig()[0])


if menu_inicio(timeout_segundos=5):
    connect_wifi(SSID, PASSWORD)
else:
    sys.exit()
