import subprocess
import os
import pyperclip
import pyautogui
import time
from pynput import keyboard
from datetime import datetime

notas_file = "noutes.sql"

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
    
    pyautogui.hotkey('ctrl', 't')
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

    pyautogui.scroll(-1000)
    time.sleep(3)
    # blank space click
    pyautogui.click(1156, 457)
    pyautogui.hotkey('enter')
    # guardar cambios
    time.sleep(2)
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
        ("dead point click", (2679, 1066)),
        ("pestana chrome", (300, 15)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)

        if nombre == "pestana chrome":
            pyautogui.mouseDown(button='left')

            # mover SIN soltar el click
            pyautogui.moveRel(925, 0, duration=0.5)
            pyautogui.moveRel(0, 400, duration=0.5)

            pyautogui.mouseUp(button='left')

            print(f"Drag en {nombre} -> ({x}, {y})")

        else:
            pyautogui.click()
            print(f"Click en {nombre} -> ({x}, {y})")

        time.sleep(0.1)

if __name__ == "__main__":
    check_all_pages()
    create_noutes()
    load_VS_code()
    