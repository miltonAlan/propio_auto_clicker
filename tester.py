import win32gui
import win32process
import psutil

def listar_ventanas_usuario():
    ventanas = []

    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            titulo = win32gui.GetWindowText(hwnd)

            if titulo.strip():
                try:
                    _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    proceso = psutil.Process(pid)

                    ventanas.append({
                        "pid": pid,
                        "nombre": proceso.name(),
                        "titulo": titulo
                    })

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    pass

    win32gui.EnumWindows(callback, None)

    vistos = set()

    print(f"{'PID':<8} {'PROCESO':<30} TITULO")
    print("-" * 100)

    for v in ventanas:
        clave = (v["pid"], v["nombre"])

        if clave not in vistos:
            vistos.add(clave)

            print(
                f"{v['pid']:<8} "
                f"{v['nombre']:<30} "
                f"{v['titulo']}"
            )

listar_ventanas_usuario()