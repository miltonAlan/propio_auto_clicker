import subprocess
import os
import pyperclip
import pyautogui
import time
from pynput import keyboard
from datetime import datetime

notas_file = "noutes.sql"

def clicker():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        # ("guardar cambios", (727, 188)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

def check_all_pages():
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

def load_VS_code():
    pasos = [
        ("3 lines", (29, 215)),
        ("archivo", (272, 224)),
        ("abrir archivo", (681, 435)),
        ("nombre del archivo", (584, 609)),
        ("abrir button", (912, 641)),
        ("blank space", (1156, 457)),
    ]
    
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(1)
    pyperclip.copy('https://vscode.dev/')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(20)

    for nombre, (x, y) in pasos:
        log(nombre)
        pyautogui.click(x, y)
        time.sleep(2)

        if nombre == "nombre del archivo":
            pyperclip.copy(str(notas_file))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

    pyautogui.hotkey('enter')
    # guardar cambios
    time.sleep(3)
    pyautogui.click(727, 188)

def create_noutes():
    subprocess.run([
        r"C:\Users\mpaucar\AppData\Local\Programs\Python\Python313\python.exe",
        r"c:\Users\mpaucar\Desktop\propio_auto_clicker\notesCreator.py"
    ])
  
def log(action):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action}")

def position_VS_code():
    pasos = [
        ("punto medio", (2326, 821)),
        ("hasta aqui", (2449, 734)),
    ]

    pyautogui.keyDown('win')
    for _ in range(5):
        pyautogui.press('right')
        time.sleep(1)
    pyautogui.keyUp('win')

    time.sleep(2)
    # Click sostenido desde el primer punto hasta el segundo
    pyautogui.moveTo(*pasos[0][1])
    pyautogui.mouseDown()

    pyautogui.moveTo(*pasos[1][1], duration=1)

    pyautogui.mouseUp()
    
if __name__ == "__main__":
    clicker()
    # check_all_pages()
    # create_noutes()
    # load_VS_code()
    position_VS_code()
    