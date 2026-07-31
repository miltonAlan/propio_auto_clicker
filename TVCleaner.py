import pyautogui
import time

CARGA_INICIAL = 20
CLICKS = 1
BUTTON = "left"

LIMPIAR_REPETICIONES = 12
LIMPIAR_DELAY = 3

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
    
        if nombre == "TView":
            time.sleep(CARGA_INICIAL)
            
        if nombre == "close Ad":
            # Coordenadas de los botones
            _, bx, by = PUNTOS[3]
            _, lx, ly = PUNTOS[4]

            for _ in range(LIMPIAR_REPETICIONES):
                # Clic en basurero
                pyautogui.moveTo(bx, by)
                pyautogui.click(clicks=CLICKS, button=BUTTON)

                # Clic en limpiar objetos
                pyautogui.moveTo(lx, ly)
                pyautogui.click(clicks=CLICKS, button=BUTTON)

                # Espacio y flecha abajo
                pyautogui.press("space")
                pyautogui.press("down")

                time.sleep(LIMPIAR_DELAY)

if __name__ == "__main__":
    ejecutar_pasos()