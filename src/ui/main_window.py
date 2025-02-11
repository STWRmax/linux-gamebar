from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QWidget, QPushButton, QComboBox
from PyQt5.QtCore import Qt
from modules.audio_control import change_volume, list_audio_apps, change_app_volume
from modules.discord_integration import connect_discord

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linux Game Bar")
        self.setGeometry(100, 100, 400, 300)
        
        # Hacer la ventana transparente y sin bordes
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        layout = QVBoxLayout()
        label = QLabel("¡Bienvenido a Game Bar para Linux!")
        layout.addWidget(label)

        # Botón de volumen
        volume_up = QPushButton("🔊 Subir Volumen")
        volume_up.clicked.connect(lambda: change_volume(5))
        layout.addWidget(volume_up)

        volume_down = QPushButton("🔉 Bajar Volumen")
        volume_down.clicked.connect(lambda: change_volume(-5))
        layout.addWidget(volume_down)

        # Menú desplegable para aplicaciones de audio
        self.app_selector = QComboBox()
        self.refresh_apps()
        layout.addWidget(self.app_selector)

        # Botón para refrescar la lista de aplicaciones
        refresh_button = QPushButton("🔄 Refrescar Aplicaciones")
        refresh_button.clicked.connect(self.refresh_apps)
        layout.addWidget(refresh_button)

        # Botón de Discord
        discord_button = QPushButton("🎮 Conectar a Discord")
        discord_button.clicked.connect(connect_discord)
        layout.addWidget(discord_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def refresh_apps(self):
        apps = list_audio_apps()
        self.app_selector.clear()
        self.app_selector.addItems(apps)