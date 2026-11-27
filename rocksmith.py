import subprocess

import pyautogui
from pynput import keyboard
from datetime import datetime
import threading
import time
import threading
import tkinter as tk

def log(action):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {action}")

def kill():
    comando = 'taskkill /f /im "Rocksmith2014.exe"'
    subprocess.run(comando, shell=True)

def on_press(key):
    try:
        if key.char == 'k':
            log("k - kill")
            kill()
            
    except Exception as e:
        if "has no attribute 'char'" in str(e):
            print(".")
        else:
            print(e)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
