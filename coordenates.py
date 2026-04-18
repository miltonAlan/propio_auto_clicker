import pyautogui
import time

print("Mueve el mouse para ver coordenadas. Ctrl+C para salir.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x}  Y: {y}      ", end="\r")  # ← espacios extra
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nPrograma detenido.")