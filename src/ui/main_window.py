import sys
import psutil
import time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont

class GameBar(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Linux Game Bar")
        self.setGeometry(100, 100, 500, 100)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)  # Hace la ventana transparente
        
        layout = QVBoxLayout()

        self.label = QLabel("🎮 Linux Game Bar - FPS: 0")
        self.label.setFont(QFont("Arial", 14))
        self.label.setStyleSheet("color: white; background: rgba(0, 0, 0, 150); padding: 10px; border-radius: 10px;")
        layout.addWidget(self.label)

        self.volume_up_button = QPushButton("🔊 Subir Volumen")
        self.volume_up_button.clicked.connect(lambda: self.change_volume(5))
        layout.addWidget(self.volume_up_button)

        self.volume_down_button = QPushButton("🔉 Bajar Volumen")
        self.volume_down_button.clicked.connect(lambda: self.change_volume(-5))
        layout.addWidget(self.volume_down_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.fps_timer = QTimer(self)
        self.fps_timer.timeout.connect(self.update_fps)
        self.fps_timer.start(1000)  # Actualizar cada segundo

    def change_volume(self, amount):
        print(f"🔊 Cambiando volumen en {amount}%")

    def update_fps(self):
        fps = self.get_fps()
        self.label.setText(f"🎮 Linux Game Bar - FPS: {fps}")

    def get_fps(self):
        return int(1 / (psutil.cpu_times_percent(interval=1).idle / 100))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GameBar()
    window.show()
    sys.exit(app.exec_())
