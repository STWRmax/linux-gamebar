import sys
from PyQt5.QtWidgets import QApplication
from src.ui.main_window import GameBarWindow
from src.keyboard_listener import HotkeyManager

def main():
    app = QApplication(sys.argv)
    
    # Iniciar ventana y teclas rápidas
    hotkeys = HotkeyManager()
    hotkeys.gamebar.show()
    
    # Ejecutar en un hilo separado (opcional)
    import threading
    thread = threading.Thread(target=hotkeys.run)
    thread.daemon = True
    thread.start()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()