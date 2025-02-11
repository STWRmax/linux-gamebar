import subprocess
import threading

def toggle_gamebar():
    subprocess.run(["xdotool", "key", "F12"])  # Simular tecla para mostrar/ocultar Game Bar

def listen_shortcut():
    subprocess.run(["xdotool", "keydown", "Super+G"], shell=True)
    toggle_gamebar()

threading.Thread(target=listen_shortcut).start()