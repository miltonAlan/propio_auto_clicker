import pyautogui
import pyperclip
import pandas as pd
import time
from pynput import keyboard
from datetime import datetime

# valor individual de la lista: copy(parseFloat(document.querySelector(".result-multiplier").innerText))
# lista completa: copy([...document.querySelector("div.stats.dropdown .payouts-block").querySelectorAll("*")].map(e => e.innerText).filter(t => /^\d+(\.\d+)?x?$/.test(t)))

coordenadas = [
    ("dead_point_click", (3157, 1069)),
    ("label_apuestas", (2665, 685)),
    ("label_anterior", (2787, 685)),
    ("dev_tools", (2865, 1039)),
]

def data_intake():
    for nombre, (x, y) in coordenadas:
        pyautogui.moveTo(x, y)
        pyautogui.click()

        if nombre == "dev_tools":
            time.sleep(0.5)
            pyautogui.press("up")
            pyautogui.press("enter")

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            data_intake()

    except Exception as e:
        print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()