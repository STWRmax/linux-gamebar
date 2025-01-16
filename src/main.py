import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import GameBar  # Importa la interfaz

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameBar()
    window.show()
    sys.exit(app.exec_())
