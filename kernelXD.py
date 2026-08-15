import pyperclip
import pyautogui
import time
from pynput import keyboard
from datetime import datetime

def checkAllPages():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            for pagina in range(1, 9):
                pyautogui.hotkey('ctrl', str(pagina))
                log(f"Página {pagina}")
                time.sleep(1) #HERE

def VSCode():
    pasos = [
        ("3 lines", (29, 215)),
        ("archivo", (272, 224)),
        ("abrir archivo", (681, 435)),
        ("nombre del archivo", (584, 609)),
        ("abrir button", (912, 641)),
        ("blank space", (1156, 457)),
    ]
    
    pyautogui.hotkey('ctrl', 't')
    time.sleep(1)
    pyperclip.copy('https://vscode.dev/')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(10)

    for nombre, (x, y) in pasos:
        log(nombre)
        pyautogui.click(x, y)
        time.sleep(2)

        if nombre == "nombre del archivo":
            pyperclip.copy("propio.sql")
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

    pyautogui.scroll(-1000)
    time.sleep(3)
    # Blank space
    pyautogui.click(1156, 457)
     
    # Ctrl + Shift + Home
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.press('home')
    
    # Soltar Ctrl + Shift
    pyautogui.keyUp('shift')
    pyautogui.keyUp('ctrl')

    
def log(action):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action}")


if __name__ == "__main__":
    checkAllPages()
    VSCode()