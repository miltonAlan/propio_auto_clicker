import time
import random
import pyautogui
from datetime import datetime
import subprocess

# dejar en false sino se desactiva con el mouse en la esquina
pyautogui.FAILSAFE = False
DEBUG = False          # False = modo normal
DEBUG_WAIT = 10        # segundos de espera en modo debug

def log(msg):
    hora = datetime.now().strftime("%H:%M:%S")
    print(f"[{hora}] {msg}")


def esperar(segundos, mensaje="esperando"):

    while segundos > 0:

        mins, secs = divmod(segundos, 60)

        tiempo = f"{mins:02}:{secs:02}"

        print(f"\r[{datetime.now().strftime('%H:%M:%S')}] {mensaje}: {tiempo}", end="")

        time.sleep(1)

        segundos -= 1

    print()  # salto línea

def formatear_duracion(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60

    if horas:
        return f"{horas}h {minutos}m {segundos_restantes}s"
    elif minutos:
        return f"{minutos}m {segundos_restantes}s"
    else:
        return f"{segundos_restantes}s"

def pausa(segundos, mensaje="esperando"):
    if DEBUG:
        log(
            f"[DEBUG] Tiempo simulado: "
            f"{formatear_duracion(segundos)} "
            f"-> esperando solo {DEBUG_WAIT}s"
        )
        esperar(DEBUG_WAIT, f"[DEBUG] {mensaje}")
    else:
        esperar(segundos, mensaje)

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
    
while True:

    log("abriendo emulador...")

    pyautogui.click(1000, 750)
    log("dead point")
    pausa(100, "esperando click emulador")
    pyautogui.click(721, 749)
    log("emulador")
    # esperar carga inicial
    pausa(60, "cargando emulador")
    log("nueva iteracion")

    # abrir long term
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(790, 300)
    log("long term")
    pausa(300, "long term activo")

    # long term window
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(760, 750)
    log("grindr")
    pausa(15, "esperando ventana emulador") 

    # home button
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(430, 660)
    log("grindr")
    esperar(15, "esperando home button") 

    # grindr icon
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(330, 170)
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

    pausa(espera, "uso app")

    # kill and start over
    comando = 'taskkill /f /im "HD-Player.exe" /im "HD-MultiInstanceManager.exe" /im "AnyDesk.exe"'
    subprocess.run(comando, shell=True)
    
    # get anydesk back
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(610, 750)
    esperar(15, "esperando anydesk")
    
    # back to console
    pyautogui.click(1000, 750)
    log("dead point")    
    pyautogui.click(650, 750)
    esperar(15, "esperando CMD")

    pausa(int(espera * 9), "esperando siguiente ciclo")
