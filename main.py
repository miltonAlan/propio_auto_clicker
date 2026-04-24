import pyautogui
import time
from pynput import keyboard

def taking_notes():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("Chrome icon", (1569, 1063)),
        ("inside chrome", (1675, 975)),   # ajusta si hace falta
        ("Chrome Tab VSCode", (2496, 17)),
        ("inside VSCode", (2728, 950))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)
        # 🔽 Scroll hacia abajo d-espués de la secuencia
    print("Haciendo scroll hacia abajo...")
    pyautogui.scroll(-600)

def taking_call_audio():
    pasos = [
        ("dead point click", (2679, 1066)),
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

def dial_out():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("dial out button", (162, 160)), 
        ("text box", (151, 296)) # no cambiar
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

        if nombre == "text box":
            time.sleep(0.5)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            pyautogui.press('enter')
            print("placing a call")            

def mute_unmute():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("B1 channel", (2556, 878)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)       

def taking_call_video():
    pasos = [
        ("dead point click", (2679, 1066)),
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
        ("dead point click", (2679, 1066)),
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

def intro_ENG():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("Brave", (1600, 1067)),
        ("ENG", (2269, 179)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.5)

        # 👉 Presionar SPACE para reproducir greeting
        if nombre == "ENG":
            time.sleep(0.1)
            pyautogui.press('space')
            print("SPACE presionado")

def volume_up():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)

    pyautogui.scroll(1)
    print("volume up")        

def volume_down():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)

    pyautogui.scroll(-1)
    print("volume down")   

def edge():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),        
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)

def close_call_audio():
    pasos = [
        ("dead point click", (2679, 1066)),
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
        ("dead point click", (2679, 1066)),
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

def deepL():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),     
        ("3x click", (2376, 1031)), 
        ("3x click", (2376, 1031)), 
        ("3x click", (2376, 1031)), 
        ("deepL", (1615, 1031))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)          


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
            print("\nF6 presionado → intro ENG...")
            intro_ENG()
        if key == keyboard.Key.f8:
            print("\nF8 presionado → intro ESP...")
            intro_ESP()
        if key == keyboard.Key.f9:
            print("\nF9 presionado → taking video call...")
            taking_call_video()
        if key == keyboard.Key.f10:
            print("\nF10 presionado → closing video call...")
            close_call_video()
        if key.char == '-':
            volume_down()
            print("Menos presionado")
        if key.char == '*':
            volume_up()
            print("Más presionado")
        if key.char == '/':
            dial_out()
            print("/ presionado")
        if key.char == '`' or key.char == '|':
            mute_unmute()
            print("Se presionó ` o |")        
        if key.char == ';':
            edge()
            print("Se presionó ;")
        if key.char == ']':
            deepL()
            print("Se presionó ]")            

    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()