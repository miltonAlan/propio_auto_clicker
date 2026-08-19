import pyautogui
import time

CLICKS = 1
BUTTON = "left"

LIMPIAR_REPETICIONES = 12
LIMPIAR_DELAY = 5

PUNTOS = [
    ("publicidad",      2603, 215),
    ("basurero",        1389, 659),
    ("limpiar objetos", 1538, 661),
]

def ejecutar_pasos():

    for _ in range(LIMPIAR_REPETICIONES):
        time.sleep(LIMPIAR_DELAY)
        for nombre, x, y in PUNTOS:
            print(f"► {nombre}")
            time.sleep(1)
            pyautogui.moveTo(x, y)
            pyautogui.click(clicks=CLICKS, button=BUTTON)
        pyautogui.press("space")

def open_TV():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("TView", (1796, 1061)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

    time.sleep(30)


if __name__ == "__main__":
    ejecutar_pasos()