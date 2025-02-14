import sys
from PyQt5.QtWidgets import QApplication

# Importar desde subcarpetas de src
from ui.main_window import GameBarWindow
# Si necesitas algo de modules, ej: from modules.audio_control import change_volume

def main():
    app = QApplication(sys.argv)
    window = GameBarWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
