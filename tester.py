import psutil

print("Procesos principales abiertos por el usuario:\n")

for proc in psutil.process_iter(['name']):
    try:
        # Solo procesos con ventana visible
        if proc.info['name']:
            pid = proc.pid

            # Verificar si tiene ventana principal visible
            import win32gui
            import win32process

            def callback(hwnd, windows):
                if win32gui.IsWindowVisible(hwnd):
                    _, found_pid = win32process.GetWindowThreadProcessId(hwnd)

                    if found_pid == pid:
                        title = win32gui.GetWindowText(hwnd)

                        if title.strip():
                            windows.append((proc.info['name'], pid, title))

            windows = []
            win32gui.EnumWindows(callback, windows)

            for w in windows:
                print(w)

    except:
        pass