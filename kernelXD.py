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
        # ("chrome", (200, 757)),
        # ("guardar cambios", (727, 188)),
        
        # edge
        ("edge", (1531, 1063)),        
        ("dead point inside edge", (2402, 980)),
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
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("3 lines", (29, 215)),
        ("nombre del archivo", (584, 609)),
        ("abrir button", (912, 641)),
        ("blank space", (1156, 457)),
    ]
    

    for nombre, (x, y) in pasos:
        log(nombre)
        pyautogui.click(x, y)
        time.sleep(2)

        if nombre == "inside":
            pyautogui.hotkey('ctrl', 'n')
            time.sleep(1)
            pyperclip.copy('https://vscode.dev/')
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')
            time.sleep(20)
        
        if nombre == "3 lines":
            pyautogui.press('down')
            pyautogui.press('right')
            pyautogui.press('down', presses=4)
            pyautogui.press('enter')
            
            
        if nombre == "nombre del archivo":
            pyperclip.copy(str(notas_file))
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)

    pyautogui.hotkey('enter')
    # guardar cambios
    time.sleep(3)
    pyautogui.click(727, 188)
    time.sleep(2)

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
    
def edge_setup():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),        
        ("inside", (2402, 980)),
        ("continue on browser", (1923, 612)),
        ("unirse ahora", (2174, 938)),
        ("tres puntitos", (1821, 200)),
        ("grabar y transcribir", (2039, 701)),
        ("iniciar transcripcion", (1967, 825)),
        ("confirmar", (2204, 701)),
        ("microfono", (2072, 202)),
        ("extender panel transcripcion", (1884, 683)),
        ("cierro dialogo", (2402, 417)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(1)
        if nombre == "edge":  # espero cargue la reunion
            time.sleep(10)
        if nombre == "inside": 
            pyautogui.press('esc')        
        if nombre == "continue on browser": 
            time.sleep(30)
            pyautogui.scroll(-500)
        if nombre == "unirse ahora": 
            time.sleep(20)
        if nombre == "microfono": 
            time.sleep(5)
        if nombre == "extender panel transcripcion": 
            time.sleep(10)
            pyautogui.click()
            pyautogui.click()

def brave_setup():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
        ("morning", (2352, 154)),
        ("afternoon", (2444, 157)),
    ]

    for nombre, (x, y) in pasos:
        time.sleep(1)
        if nombre == "morning":
            if datetime.now().hour < 12:
                time.sleep(5)
                pyautogui.moveTo(x, y)
                pyautogui.click()

                pyautogui.rightClick(x, y)
                pyautogui.press("down")
                pyautogui.press("enter")

        elif nombre == "afternoon":
            if datetime.now().hour >= 12:
                time.sleep(5)
                pyautogui.moveTo(x, y)
                pyautogui.click()

                pyautogui.rightClick(x, y)
                pyautogui.press("down")
                pyautogui.press("enter")

        else:
            pyautogui.moveTo(x, y)
            pyautogui.click()
            
    # cierro pestania en blanco
    pyautogui.hotkey("ctrl", "w")
    # espero carguen todas las pantallas
    time.sleep(10)
            
def audios_checkup():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
    ]

    for nombre, (x, y) in pasos:
        time.sleep(1)
        pyautogui.moveTo(x, y)
        pyautogui.click()
        
    #EN
    time.sleep(2)
    pyautogui.hotkey("ctrl", "1")
    pyautogui.press("space")
    #ES
    pyautogui.hotkey("ctrl", "2")
    time.sleep(2)
    pyautogui.press("space")
    #TXS    
    time.sleep(2)
    pyautogui.hotkey("ctrl", "3")
    pyautogui.press("space")
                        
def menu_principal():
    while True:
        print("\n" + "=" * 50)
        print("              MENÚ PRINCIPAL")
        print("=" * 50)
        print("  0. Ejecutar TODAS las secciones")
        print("  1. Utilitario")
        print("  2. Revisión general")
        print("  3. VS Code")
        print("  4. Transcripción")
        print("  5. Introducción de audios")
        print("  Q. Salir")
        print("=" * 50)

        opcion = input("Selecciona una opción: ").strip().lower()

        # ============================================================
        # SALIR
        # ============================================================
        if opcion == "q":
            print("\nSaliendo...")
            break

        # ============================================================
        # OPCIÓN 0
        # TODAS LAS SECCIONES EXCEPTO UTILITARIO
        # ============================================================
        if opcion == "0":
            print("\n>>> EJECUTANDO TODAS LAS SECCIONES <<<\n")

            # Revisión general
            print(">>> REVISIÓN GENERAL")
            check_all_pages()

            # VS Code
            print(">>> VS CODE")
            create_noutes()
            load_VS_code()
            position_VS_code()

            # Transcripción
            print(">>> TRANSCRIPCIÓN")
            edge_setup()

            # Introducción de audios
            print(">>> INTRODUCCIÓN DE AUDIOS")
            brave_setup()
            audios_checkup()

            print("\n>>> TODAS LAS SECCIONES FINALIZADAS <<<")

        # ============================================================
        # OPCIONES INDIVIDUALES / COMBINADAS
        # ============================================================
        else:
            # Separar usando "."
            # Ejemplos:
            # 1.2
            # 2.3.5
            # 1.2.3.4.5
            opciones = opcion.split(".")

            opciones_validas = {"1", "2", "3", "4", "5"}

            # Validar
            if not all(op in opciones_validas for op in opciones):
                print("\n❌ Opción inválida.")
                print("\nEjemplos válidos:")
                print("  0")
                print("  1")
                print("  2")
                print("  1.2")
                print("  2.3.5")
                print("  1.2.3.4.5")
                continue

            # Eliminar duplicados manteniendo el orden
            opciones = list(dict.fromkeys(opciones))

            print(f"\n>>> EJECUTANDO: {'.'.join(opciones)} <<<\n")

            # ========================================================
            # 1 - UTILITARIO
            # ========================================================
            if "1" in opciones:
                print(">>> UTILITARIO")
                clicker()

            # ========================================================
            # 2 - REVISIÓN GENERAL
            # ========================================================
            if "2" in opciones:
                print(">>> REVISIÓN GENERAL")
                check_all_pages()

            # ========================================================
            # 3 - VS CODE
            # ========================================================
            if "3" in opciones:
                print(">>> VS CODE")

                create_noutes()
                load_VS_code()
                position_VS_code()

            # ========================================================
            # 4 - TRANSCRIPCIÓN
            # ========================================================
            if "4" in opciones:
                print(">>> TRANSCRIPCIÓN")

                edge_setup()

            # ========================================================
            # 5 - INTRODUCCIÓN DE AUDIOS
            # ========================================================
            if "5" in opciones:
                print(">>> INTRODUCCIÓN DE AUDIOS")

                brave_setup()
                audios_checkup()

            print("\n>>> SELECCIÓN FINALIZADA <<<")

        input("\nPresiona ENTER para volver al menú...")


if __name__ == "__main__":
    menu_principal()
    
    