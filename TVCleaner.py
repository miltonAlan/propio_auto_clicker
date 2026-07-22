import pyautogui
import time

CLICK_DELAY = 0.5      # Espera después de cada clic
CLICKS = 1              # Cantidad de clics
BUTTON = "left"         # left, right, middle

LIMPIAR_REPETICIONES = 12    # Veces que se presiona Espacio + Flecha abajo
LIMPIAR_DELAY = 2         # Espera entre cada repetición

PUNTOS = [
    ("dead point",      3000, 1060),
    ("TView",           1787, 1067),
    ("close Ad",        2601, 210),
    ("basurero",        1389, 659),
    ("limpiar objetos", 1538, 661),
]

def ejecutar_pasos():

    for nombre, x, y in PUNTOS:
        print(f"► {nombre}")
        pyautogui.moveTo(x, y)
        pyautogui.click(clicks=CLICKS, button=BUTTON)

        if nombre == "close Ad":
            for _ in range(LIMPIAR_REPETICIONES):
                pyautogui.press("space")
                pyautogui.press("down")
                time.sleep(LIMPIAR_DELAY)

        time.sleep(CLICK_DELAY)

if __name__ == "__main__":
    ejecutar_pasos()