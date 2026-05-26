import time
import random
import pyautogui
from datetime import datetime
import subprocess

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
        return random.randint(1440, 2160)   # 24m - 36m

    # Mañana
    elif 6 <= hora < 12:
        return random.randint(1620, 2160)   # 27m - 36m

    # Tarde
    elif 12 <= hora < 19:
        return random.randint(1080, 1800)   # 18m - 30m

    # Noche (más activo)
    else:
        return random.randint(720, 1440)    # 12m - 24m
    
# =========================================================
# LOOP PRINCIPAL
# =========================================================

while True:

    log("abriendo emulador...")

    pyautogui.click(1000, 750)
    log("dead point")
    esperar(100, "esperando click emulador")
    pyautogui.click(721, 749)
    log("emulador")
    # esperar carga inicial
    esperar(60, "cargando emulador")
    log("nueva iteracion")

    # abrir long term
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(800, 208)
    log("long term")
    esperar(300, "long term activo")
    #esperar(15, "long term activo") # BORRAR

    # abrir app
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(760, 742)
    log("grindr")
    esperar(15, "esperando grindr") 

    # back to console
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(650, 750)
    esperar(15, "esperando CMD")

    # tiempo aleatorio humano
    espera = tiempo_humano()

    minutos = round(espera / 60, 1)

    log(f"uso humano simulado: {minutos} minutos")

    esperar(espera, "uso app")
    #esperar(100, "uso app") # BORRAR

    # kill and start over
    comando = 'taskkill /f /im "HD-Player.exe" /im "HD-MultiInstanceManager.exe"'
    subprocess.run(comando, shell=True)

    # esperar(15, "esperando siguiente ciclo") # BORRAR
    esperar(int(espera * 2.1), "esperando siguiente ciclo");