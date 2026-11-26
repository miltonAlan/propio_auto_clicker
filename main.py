import pyautogui
from pynput import keyboard
from datetime import datetime
import threading
import time
import threading
import tkinter as tk

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
    
    pyautogui.scroll(-400)

def newTab():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("Chrome icon", (1569, 1063)),
        ("inside chrome", (1675, 975)),   
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
    
    pyautogui.hotkey('ctrl', 't')

def googleThat():

    pyautogui.press('backspace')
    time.sleep(0.1)

    pyautogui.hotkey('shift', 'home')
    time.sleep(0.1)

    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.1)
    
    pyautogui.hotkey('ctrl', 't')
    time.sleep(0.1)
    
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.1)
    
    pyautogui.hotkey('enter')

def taking_call_audio():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("accept call", (1100, 682)), 
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside again", (150, 660)),
        ("intake questions", (561, 510)),
    ]
    
    reset_volume()

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')

        if nombre == "A3":
            intro_ENG()
        
        if nombre == "inside again":
            time.sleep(3)

def hangUpLEP():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("x", (1292, 415)),
        ("remove caller", (856, 512)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            pyautogui.hotkey('ctrl', '5')

def music_mode_ON():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("youtube", (1492, 1061)),
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),   
        ("A3 aux", (2932, 838)),
        ("B1 aux", (2937, 871)),
    ]

    for nombre, (x, y) in pasos:
        if nombre == "youtube":
            pyautogui.press('space')
            time.sleep(0.2)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.press('space')
            
        else: 
            time.sleep(0.2)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            
def music_mode_OFF():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),   
        ("A3 aux", (2932, 838)),
        ("B1 aux", (2937, 871)),
        ("dead point click", (2679, 1066)),
        ("youtube", (1492, 1061)),
    ]

    for nombre, (x, y) in pasos:
        if nombre == "youtube":
            pyautogui.press('space')
            time.sleep(0.2)
            pyautogui.moveTo(x, y)
            pyautogui.click()
            time.sleep(0.2)
            pyautogui.press('space')
            
        else: 
            time.sleep(0.2)
            pyautogui.moveTo(x, y)
            pyautogui.click()            

def back_from_night_mode():
    jabra_on_off()
    taking_call_audio()

def backToActive():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("dead point inside", (157, 143)),
        ("Go Online", (1278, 152)),
        ("start taking calls", (1165, 733)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            pyautogui.hotkey('ctrl', '5')
        
        if nombre == "dead point inside":
            pyautogui.hotkey('esc')
            time.sleep(0.5)
            
def back_to_business():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("Chrome icon", (1569, 1063)),
        ("inside chrome", (1675, 975)), 
    ]

    # for nombre, (x, y) in pasos:

    taking_notes()
    pyautogui.hotkey('ctrl', 'tab')

def back_to_portal():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')

def dial_out():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), 
        ("add participant", (659, 469)), 
        ("text box", (1169, 362)), 
        ("call button", (1266, 493)) 
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
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')

        if nombre == "text box":
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')

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
        time.sleep(0.1)

        if nombre == "blank space":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '6')  
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

def jabra_on_off():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("A3 jabra", (2821, 841)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

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

    for _ in range(12): pyautogui.scroll(-1)

def taking_call_video():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("accept call", (948, 478)), 
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        # Scroll down for intake form
        ("dead point click", (2679, 1066)),
        ("chrome", (200, 757)),
        ("inside again", (150, 660)),
        ("dead point chrome", (773, 178)),
    ]

    reset_volume()

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')
    time.sleep(3)       
    pyautogui.scroll(-200)

def intro_ESP():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "brave":
            time.sleep(0.1)
            hora = datetime.now().hour
            pestaña = "2" if hora < 12 else "4"

            pyautogui.hotkey("ctrl", pestaña)
            pyautogui.click(2503, 279)
           
    threading.Thread(
        target=alerta_demorada,
        args=(10,),
        daemon=True
    ).start()                

def hang_up_with_audio():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
    ]

    # jabra_on_off()
    volume_down() #no quitar estoy sino no funciona el click
    pyautogui.click(button="right")
    pyautogui.write("-59")
    pyautogui.press("enter")

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "brave":
            time.sleep(0.1)
            pyautogui.hotkey("ctrl", "5")
            pyautogui.click(2503, 279)
            
    time.sleep(7)
    jabra_on_off()
    close_call_audio()

def alerta_demorada(tiempo):
    time.sleep(tiempo)
    alerta_visual()

def intro_ENG():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "brave":
            time.sleep(0.1)
            hora = datetime.now().hour
            pestaña = "1" if hora < 12 else "3"

            pyautogui.hotkey("ctrl", pestaña)
            pyautogui.click(2503, 279)
            
    threading.Thread(
        target=alerta_demorada,
        args=(12,),
        daemon=True
    ).start()       

def volume_up():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

    pyautogui.scroll(1)

def reset_volume_aux():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2880, 829)),
        ("volume bar", (2880, 829)),
        ("volume bar", (2880, 829)),
        ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
    
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
    
    pyautogui.scroll(-1)

def volume_down(cantidad=-1):
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),        
        ("volume bar", (2765, 844)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

    pyautogui.scroll(cantidad)

def edge():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("edge", (1531, 1063)),        
        ("dead point inside edge", (2402, 980)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.1)

def hold_time():
    taking_notes()
    hora_actual = datetime.now().strftime("%H..%M..%S")
    print(hora_actual)          
    pyautogui.write(hora_actual)  

def close_call_audio():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)),
        ("hang up button", (1285, 155)), 
        ("END", (895, 515)), 
        ("successfully", (830, 523)),
        ("submit", (1258,685)),
        ("yes, submit", (882,514))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '5')
            
        if nombre == "END":
            time.sleep(1)
            
        if nombre == "successfully":
            time.sleep(0.3)
            pyautogui.scroll(-2500)
            pyautogui.scroll(-2500)

def close_call_video():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("voicemeter icon", (1678, 1060)),
        ("A3", (2813, 838)),
        ("chrome", (200, 757)),
        ("inside", (150, 660)), 
        ("hang up button", (217, 678)), 
        ("successfully", (119, 217)),
        ("save n close", (1236,650)),
        ("save n close x2", (1135,493))
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time.sleep(0.2)

        if nombre == "inside":
            time.sleep(0.1)
            pyautogui.hotkey('ctrl', '4')

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

        else:
            pyautogui.click()

        time.sleep(0.1)
    # boton traducir deepL
    pyautogui.click(1530, 346)

def audios_health_check():
    pasos = [
        ("dead point click", (2679, 1066)),
        ("brave", (1600, 1067)),
    ]

    for nombre, (x, y) in pasos:
        pyautogui.moveTo(x, y)
        pyautogui.click()
        
        if nombre == "brave":
            for i in range(1, 6):
                pyautogui.hotkey("ctrl", str(i))
                pyautogui.hotkey("ctrl", "r")

def log(action):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action}")



def alerta_visual(duracion=1000, color="#EEFA00"):
    ventana = tk.Tk()
    ventana.overrideredirect(True)
    ventana.attributes("-topmost", True)
    ventana.attributes("-alpha", 0.8)

    ventana.configure(bg=color)

    # Pantalla completa
    pantalla_ancho = ventana.winfo_screenwidth()
    pantalla_alto = ventana.winfo_screenheight()

    ventana.geometry(f"{pantalla_ancho}x{pantalla_alto}+0+0")

    ventana.after(duracion, ventana.destroy)
    ventana.mainloop()



def pausas_activas():
    while True:
        time.sleep(45 * 60)  # Esperar 45 minutos
        alerta_visual(duracion=60000, color="#00BFFF")

def on_press(key):
    try:
        if key == keyboard.Key.f2:
            log("F2 - dial_out")
            dial_out()

        if key == keyboard.Key.f4:
            log("F4 - taking_notes")
            taking_notes()

        if key == keyboard.Key.print_screen:
            log("PrintScreen - volume_up")
            volume_up()

        if key == keyboard.Key.page_down:
            log("PageDown - audios_health_check")
            audios_health_check()

        if key == keyboard.Key.page_up:
            log("PageUp - night_mode")
            night_mode()

        if key == keyboard.Key.f6:
            log("F6 - intro_ENG")
            threading.Thread(
                target=alerta_visual,
                kwargs={"duracion": 1000, "color": "#04FF2E"},
                daemon=True
                ).start()
            intro_ENG()

        if key == keyboard.Key.f8:
            log("F8 - intro_ESP")
            threading.Thread(
                target=alerta_visual,
                kwargs={"duracion": 1000, "color": "#04FF2E"},
                daemon=True
                ).start()
            intro_ESP()

        if key == keyboard.Key.f9:
            log("F9 - gpt")
            gpt()

        if key == keyboard.Key.menu:
            log("options - newTab")
            newTab()
        
        if key == keyboard.Key.f10:
            log("f10 - hang_up_with_audio")
            hang_up_with_audio()  

        if key == keyboard.Key.scroll_lock:
            log("ScrollLock - volume_down")
            volume_down()

        if key.char == '-':
            log("- - close_call_audio")
            pyautogui.press('backspace')            
            close_call_audio()

        if key.char == '*':
            log("* - taking_call_audio")
            pyautogui.press('backspace')   
            taking_call_audio()

        if key.char == '`' or key.char == '|':
            log("` or | - mute_unmute")
            pyautogui.press('backspace')   
            mute_unmute()

        if key.char == ';':
            log("; - edge")
            pyautogui.press('backspace')   
            edge()

        if key.char == ']':
            log("] - deepL")
            pyautogui.press('backspace')   
            deepL()

        if key.char == '[':
            log("[ - hold_time")
            pyautogui.press('backspace')   
            hold_time()

        if key.char == "'":
            log("' - jabra_on_off")
            pyautogui.press('backspace')   
            jabra_on_off()
            
        if key.char == '/':
            log("/ - hang up LEP")
            pyautogui.press('backspace')   
            hangUpLEP()
        
        if key.char == '+':
            log("+ - back to active")
            pyautogui.press('backspace')   
            backToActive()
        
        if key.char == "\\":
            log("\\ - back_to_business")
            pyautogui.press('backspace')   
            back_to_business()
        
        if key.char == '&':
            log("& - music mode ON")
            pyautogui.press('backspace')   
            music_mode_ON()
            reset_volume_aux()
        
        if key.char == '^':
            log("^ - music mode OFF")
            pyautogui.press('backspace')   
            music_mode_OFF()
        
        if key.char == '!':
            log("! - back_from_night_mode")
            pyautogui.press('backspace')   
            back_from_night_mode()
            
    except Exception as e:
        if "has no attribute 'char'" in str(e):
            print(".")
        else:
            print(e)

# Iniciar recordatorios de pausas activas
threading.Thread(
    target=pausas_activas,
    daemon=True
).start()

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
