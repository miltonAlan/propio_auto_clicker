import pyautogui
import time
from datetime import datetime
from pynput import keyboard

marcado = False

def on_press(key):
    global marcado

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        if not marcado:
            marcado = True
            x, y = pyautogui.position()
            timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(f"\n[{timestamp}] MARCA -> X: {x}  Y: {y}")

def on_release(key):
    global marcado

    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        marcado = False

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

print("Mueve el mouse para ver coordenadas. Presiona Ctrl para guardar una marca. Ctrl+C para salir.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}  Y: {y}      ", end="\r")
        time.sleep(0.05)
except KeyboardInterrupt:
    listener.stop()
    print("\nPrograma detenido.")