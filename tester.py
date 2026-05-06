# PRUEBA DE SCROLL LOCK - múltiples métodos

import keyboard as kb
from pynput import keyboard as pynput_keyboard

print("Presiona Scroll Lock para probar...\n")

# ===== MÉTODO 1: pynput =====
def on_press(key):
    try:
        print(f"[pynput] key: {key}")

        if key == pynput_keyboard.Key.scroll_lock:
            print("✅ pynput detectó Scroll Lock")

    except Exception as e:
        print(f"[pynput ERROR]: {e}")

listener = pynput_keyboard.Listener(on_press=on_press)
listener.start()


# ===== MÉTODO 2: keyboard (hotkey) =====
kb.add_hotkey('scroll lock', lambda: print("✅ keyboard.add_hotkey detectó Scroll Lock"))

# ===== MÉTODO 3: keyboard (evento directo) =====
def on_event(e):
    if e.name == 'scroll lock':
        print("✅ keyboard event detectó Scroll Lock")

kb.on_press(on_event)

# ===== MÉTODO 4: variantes =====
kb.add_hotkey('scrlk', lambda: print("✅ 'scrlk' funcionó"))
kb.add_hotkey('scroll', lambda: print("✅ 'scroll' funcionó"))


# 🔒 BLOQUEO REAL (esto evita que el script termine)
print("\nEscuchando... (Ctrl + C para salir)\n")

try:
    while True:
        kb.wait()  # espera eventos continuamente
except KeyboardInterrupt:
    print("\nSaliendo...")