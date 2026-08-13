import pyautogui
import time

CLICKS = 1
BUTTON = "left"

LIMPIAR_REPETICIONES = 12
LIMPIAR_DELAY = 5

PUNTOS = [
    ("basurero",        1389, 659),
    ("limpiar objetos", 1538, 661),
]

def ejecutar_pasos():

    for _ in range(LIMPIAR_REPETICIONES):
        for nombre, x, y in PUNTOS:
            print(f"► {nombre}")
            pyautogui.moveTo(x, y)
            pyautogui.click(clicks=CLICKS, button=BUTTON)
        pyautogui.press("space")
        time.sleep(LIMPIAR_DELAY)

if __name__ == "__main__":
    ejecutar_pasos()