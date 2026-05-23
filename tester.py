import subprocess

comando = 'taskkill /f /im "HD-Player.exe" /im "HD-MultiInstanceManager.exe"'

subprocess.run(comando, shell=True)