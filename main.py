import pyautogui
import time
from pynput import keyboard

def taking_notes():
    pasos = [
        ("Chrome", (1569, 1063)),
        ("VS Code", (1675, 975)),   # ajusta si hace falta
        ("Chrome Tab VSCode", (2503, 10)),
        ("inside VSCode", (2728, 498))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)
        # 🔽 Scroll hacia abajo después de la secuencia
    print("Haciendo scroll hacia abajo...")
    pyautogui.scroll(-500)

def taking_call_audio():
    pasos = [
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("accept call", (948, 478)), 
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("Brave", (1600, 1067)),
        ("ENG", (2275, 175)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')
            print("Ctrl + 5 ejecutado")

        # 👉 Presionar SPACE para reproducir greeting
        if nombre == "ENG":
            time.sleep(1)
            pyautogui.press('space')
            print("SPACE presionado")

def taking_call_video():
    pasos = [
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("accept call", (948, 478)), 
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')
            print("Ctrl + 5 ejecutado")

def intro_ESP():
    pasos = [
        ("Brave", (1600, 1067)),
        ("ESP", (2269, 209)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Presionar SPACE para reproducir greeting
        if nombre == "ESP":
            time.sleep(0.1)
            pyautogui.press('space')
            print("SPACE presionado")

def close_call_audio():
    pasos = [
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("hang up button", (200, 450)), 
        ("END", (944, 487)), # pilas no cambiar el nombre
        ("successfully", (422, 210)),
        ("save n close", (1236,650)),
        ("save n close x2", (1135,493))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')
            print("Ctrl + 5 ejecutado")
        if nombre == "END":
            # time.sleep(0.1)
            print("Haciendo scroll hacia abajo...")
            pyautogui.scroll(-2500)
            pyautogui.scroll(-2500)
            time.sleep(0.1)

def close_call_video():
    pasos = [
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("hang up button", (217, 678)), 
        ("successfully", (119, 217)),
        ("save n close", (1236,650)),
        ("save n close x2", (1135,493))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')
            print("Ctrl + 5 ejecutado")

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            print("\nF2 presionado → taking notes...")
            taking_notes()
        if key == keyboard.Key.f3:
            print("\nF3 presionado → taking audio call...")
            taking_call_audio()
        if key == keyboard.Key.f4:
            print("\nF4 presionado → closing audio call...")
            close_call_audio()
        if key == keyboard.Key.f6:
            print("\nF6 presionado → taking video call...")
            taking_call_video()
        if key == keyboard.Key.f7:
            print("\nF7 presionado → closing video call...")
            close_call_video()
        if key == keyboard.Key.f8:
            print("\nF8 presionado → intro ESP...")
            intro_ESP()
    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()