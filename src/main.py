import sys
from PyQt5.QtWidgets import QApplication
from ui.main_window import MainWindow
from ui.floating_hud import FloatingHUD

app = QApplication(sys.argv)
window = MainWindow()
hud = FloatingHUD()
window.show()
hud.show()
sys.exit(app.exec_())