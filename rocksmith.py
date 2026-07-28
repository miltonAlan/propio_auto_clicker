import time
import pyautogui

PUNTOS = [
    ((3000, 1060), False),
    ((1787, 1067), False),
    ((2601, 210),  True),
    ((1389, 659), False),
    ((1538, 661), False),
]

def ejecutar():
    for pos, ejecutar_ciclo in PUNTOS:
        pyautogui.click(*pos)

        if ejecutar_ciclo:
            time.sleep(20)

            for _ in range(12):
                pyautogui.click(*PUNTOS[3][0])
                pyautogui.click(*PUNTOS[4][0])
                pyautogui.press("space")
                pyautogui.press("down")
                time.sleep(2)

def main():
    ejecutar()

if __name__ == "__main__":
    main()