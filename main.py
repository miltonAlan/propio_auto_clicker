import pyautogui
import time
from pynput import keyboard
from datetime import datetime

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
        # scroll for intake form;
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside again", (150, 660)),
        ("dead point chrome", (773, 178)),
    ]
    
    reset_volume()

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')

        # 👉 Presionar SPACE para reproducir greeting
        if nombre == "ENG":
            time.sleep(1)
            pyautogui.press('space')
            print("SPACE presionado")

    time.sleep(3)       
    pyautogui.scroll(-250)

def hangUpLEP():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("hang up button", (274, 626)),
        ("remove button", (961, 483)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            pyautogui.hotkey('ctrl', '4')

def backToActive():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("back to active button", (880, 415)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            pyautogui.hotkey('ctrl', '4')
            
def pronunciation():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("X button", (632, 336)),
        ("text box", (194, 345)),
        ("speaker button", (82, 619)),
    ]

    pyautogui.press('end')
    time.sleep(0.1)

    pyautogui.press('backspace')
    time.sleep(0.1)

    pyautogui.hotkey('shift', 'home')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            pyautogui.hotkey('ctrl', '7')            
        
        if nombre == "text box":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')

def back_to_portal():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')

def dial_out():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("dial out button", (162, 160)), 
        ("text box", (151, 296)) # no cambiar
    ]

    pyautogui.press('end')
    time.sleep(0.1)

    pyautogui.hotkey('shift', 'home')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')

        if nombre == "text box":
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            pyautogui.press('enter')
            print("placing a call")            

def gpt():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), 
        ("blank space", (738, 679)), 
    ]

    pyautogui.press('end')
    time.sleep(0.1)

    pyautogui.hotkey('shift', 'home')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)

        if nombre == "blank space":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')  
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.1)
            pyautogui.press('enter')
            time.sleep(0.1)

def mute_unmute():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("B1 channel", (2556, 878)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        # time.sleep(0.5)       

def jabra_on_off():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("A3 jabra", (2821, 841)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")

def night_mode():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),
        # 3x para resetear
        ("volume bar", (2765, 844)),        
        ("volume bar", (2765, 844)),        
        ("volume bar", (2765, 844)),        
    ]

    jabra_on_off()

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")

    for _ in range(12): pyautogui.scroll(-1)

def taking_call_video():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), # pilas no cambiar el nombre
        ("accept call", (948, 478)), 
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        # Scroll down for intake form
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside again", (150, 660)),
        ("dead point chrome", (773, 178)),
    ]

    reset_volume()  # Asegura que el volumen esté en un nivel conocido antes de empezar     

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')
    # Haciendo scroll hacia abajo...
    time.sleep(3)       
    pyautogui.scroll(-200)

def intro_ESP():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("Brave", (1600, 1067)),
        ("ESP", (2269, 209)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

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
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

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
        # print(f"Click en {nombre} -> ({x}, {y})")
        # time.sleep(0.1)

    pyautogui.scroll(1)

def reset_volume():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
        ("volume bar", (2765, 844)),
        ("volume bar", (2765, 844)),]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
    
    pyautogui.scroll(-1)
    # pyautogui.scroll(-1)

def volume_down():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        # time.sleep(0.1)

    pyautogui.scroll(-1)
    # print("volume down")   

def edge():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),        
        ("dead point inside edge", (2402, 980)),
        # ("3x click", (2376, 1031))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.1)

def hold_time():
    taking_notes()
    hora_actual = datetime.now().strftime("%H:%M:%S")
    pyautogui.write(hora_actual)

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
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')
        if nombre == "END":
            # time.sleep(0.1)
            print("Haciendo scroll hacia abajo...")
            pyautogui.scroll(-2500)
            pyautogui.scroll(-2500)
            time.sleep(0.1)

    # reset_volume()

def close_call_audio_with_audio():
    pasos = [
        # my pleasure audio
        ("dead point click", (2679, 1066)),
        ("Brave", (1600, 1067)),
        ("PLEASURE", (2260, 240)),

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
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        # 👉 Presionar SPACE para reproducir
        if nombre == "PLEASURE":
            pyautogui.press('space')
            time.sleep(5)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')
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
        # print(f"Click en {nombre} -> ({x}, {y})")
        time.sleep(0.2)

        # 👉 Ejecutar Ctrl + 5 cuando dentro de chrome
        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')

    # reset_volume()

def deepL():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),
        ("dead point inside edge", (2402, 980)),
        ("3x click", (2376, 1031)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)

        if nombre == "3x click":
            pyautogui.mouseDown(button='left')  # mantiene presionado

            # mover SIN soltar el click
            pyautogui.moveRel(0, -400, duration=0.2)
            pyautogui.moveRel(-925, 0, duration=0.2)

            pyautogui.mouseUp(button='left')  # suelta recién al final

            print(f"Drag en {nombre} -> ({x}, {y})")

        else:
            pyautogui.click()
            print(f"Click en {nombre} -> ({x}, {y})")

        time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'l')
    # pasos = [
    #     ("dead point click", (2679, 1066)),
    #     ("edge", (1531, 1063)),     
    #     ("3x click", (2376, 1031)), 
    #     ("3x click", (2376, 1031)), 
    #     ("3x click", (2376, 1031)), 
    #     ("deepL", (1615, 1031))
    # ]

    # for nombre, (x, y) in pasos:
    #     pyautogui.moveTo(x, y)
    #     pyautogui.click()
    #     print(f"Click en {nombre} -> ({x}, {y})")
    #     time.sleep(0.1)          

def log(action):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action}")

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            log("F2 - dial_out")
            dial_out()

        if key == keyboard.Key.f3:
            log("F3 - taking_call_video")
            taking_call_video()

        if key == keyboard.Key.f4:
            log("F4 - taking_notes")
            taking_notes()

        if key == keyboard.Key.print_screen:
            log("PrintScreen - volume_up")
            volume_up()

        if key == keyboard.Key.page_down:
            log("PageDown - back_to_portal")
            back_to_portal()

        if key == keyboard.Key.page_up:
            log("PageUp - night_mode")
            night_mode()

        if key == keyboard.Key.f6:
            log("F6 - intro_ENG")
            intro_ENG()

        if key == keyboard.Key.f8:
            log("F8 - intro_ESP")
            intro_ESP()

        if key == keyboard.Key.f9:
            log("F9 - gpt")
            gpt()

        if key == keyboard.Key.f10:
            log("F10 - close_call_video")
            close_call_video()

        if key == keyboard.Key.scroll_lock:
            log("ScrollLock - volume_down")
            volume_down()

        if key.char == '-':
            log("- - close_call_audio")
            close_call_audio()

        if key.char == '*':
            log("* - taking_call_audio")
            taking_call_audio()

        if key.char == '`' or key.char == '|':
            log("` or | - mute_unmute")
            mute_unmute()

        if key.char == ';':
            log("; - edge")
            edge()

        if key.char == ']':
            log("] - deepL")
            deepL()

        if key.char == '[':
            log("[ - hold_time")
            hold_time()

        if key.char == "'":
            log("' - jabra_on_off")
            jabra_on_off()
            
        if key.char == '/':
            log("/ - hang up LEP")
            hangUpLEP()
        
        if key.char == '+':
            log("+ - back to active")
            backToActive()
        
        if key.char == "\\":
            log("\\ - pronunciation")
            pronunciation()
            
    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
