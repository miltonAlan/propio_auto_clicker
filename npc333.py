import time
import random
import pyautogui
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

pyautogui.FAILSAFE = True

# =========================================================
# LOG
# =========================================================

def log(msg):
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora}] {msg}")


# =========================================================
# COUNTDOWN
# =========================================================
"""
Muestra conteo regresivo en consola.
"""

def esperar(segundos, mensaje="esperando"):

    while segundos > 0:

        mins, secs = divmod(segundos, 60)

        tiempo = f"{mins:02}:{secs:02}"

        print(f"\r[{datetime.now().strftime('%H:%M:%S')}] {mensaje}: {tiempo}", end="")

        time.sleep(1)

        segundos -= 1

    print()  # salto línea


# =========================================================
# TIEMPOS HUMANOS
# =========================================================

def tiempo_humano():

    hora = datetime.now().hour

    # Madrugada
    if 0 <= hora < 6:
        return random.randint(2400, 3600)   # 40m - 1h

    # Mañana
    elif 6 <= hora < 12:
        return random.randint(2700, 3600)   # 45m - 1h

    # Tarde
    elif 12 <= hora < 19:
        return random.randint(1800, 3000)   # 30m - 50m

    # Noche (más activo)
    else:
        return random.randint(1200, 2400)   # 20m - 40m


# =========================================================
# ABRIR EMULADOR
# =========================================================

log("abriendo emulador...")

pyautogui.click(1000, 750)
log("dead point")
esperar(2, "esperando click emulador")
pyautogui.click(721, 749)
log("emulador")
# esperar carga inicial
esperar(60, "cargando emulador")


# =========================================================
# LOOP PRINCIPAL
# =========================================================

while True:

    log("nueva iteracion")

    # abrir long term
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(800, 208)
    log("long term")
    # esperar(300, "long term activo")
    esperar(15, "long term activo") # BORRAR

    # abrir app
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(760, 742)
    log("grindr")

    # tiempo aleatorio humano
    espera = tiempo_humano()

    minutos = round(espera / 60, 1)

    log(f"uso humano simulado: {minutos} minutos")

    esperar(espera, "uso app")

    # volver al emulador
    #pyautogui.click(1000, 750)
    #log("dead point")
    #esperar(2, "esperando emulador")
    #pyautogui.click(721, 749)
    #log("emulador")

    #esperar(5, "cargando emulador")

    # detener long term
    #pyautogui.click(1000, 750)
    #log("dead point")    
    #pyautogui.click(800, 208)
    #log("long term STOP")

    #esperar(5, "esperando")
    #cerrar popup / ventana

    #pyautogui.click(1000, 750)
    #log("dead point")    
    #pyautogui.click(830, 370)
    #log("close button")


    esperar(espera, "esperando siguiente ciclo")