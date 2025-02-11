from PyQt5.QtCore import Qt

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

        # Botones existentes...
        volume_up = QPushButton("🔊 Subir Volumen")
        volume_up.clicked.connect(lambda: change_volume(5))
        layout.addWidget(volume_up)

        volume_down = QPushButton("🔉 Bajar Volumen")
        volume_down.clicked.connect(lambda: change_volume(-5))
        layout.addWidget(volume_down)

        discord_button = QPushButton("🎮 Conectar a Discord")
        discord_button.clicked.connect(connect_discord)
        layout.addWidget(discord_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)