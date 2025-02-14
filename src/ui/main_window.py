from PyQt5.QtCore import Qt, QTimer, QPoint
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor, QFont
from src.modules.system_monitor import SystemMonitor
from src.modules.audio_control import AudioControl
from src.modules.discord_rpc import DiscordRPC

class GameBarWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(100, 100, 800, 150)
        
        # Configuración inicial
        self.opacity = 0.9
        self.dragging = False
        self.offset = QPoint()
        
        # Widgets principales
        self.init_ui()
        self.init_system_monitor()
        self.init_audio_control()
        self.init_discord()
        
        # Actualización en tiempo real
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)
        
    def init_ui(self):
        main_widget = QWidget()
        main_layout = QHBoxLayout()
        main_layout.setSpacing(20)
        
        # Sección de rendimiento
        self.performance_widget = self.create_stats_box("CPU: 0%\nGPU: 0%\nRAM: 0%")
        
        # Sección de audio
        self.audio_widget = self.create_stats_box("Volumen: 100%\nAplicación: N/A")
        
        # Sección Discord
        self.discord_widget = self.create_stats_box("Discord: Desconectado")
        
        main_layout.addWidget(self.performance_widget)
        main_layout.addWidget(self.audio_widget)
        main_layout.addWidget(self.discord_widget)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        
    def create_stats_box(self, text):
        widget = QWidget()
        widget.setStyleSheet("""
            background-color: rgba(40, 40, 40, 0.8);
            border-radius: 10px;
            padding: 15px;
        """)
        
        label = QLabel(text)
        label.setFont(QFont("Arial", 10))
        label.setStyleSheet("color: white;")
        
        layout = QVBoxLayout()
        layout.addWidget(label)
        widget.setLayout(layout)
        return widget
        
    def update_stats(self):
        # Actualizar métricas del sistema
        cpu = SystemMonitor.get_cpu_usage()
        gpu = SystemMonitor.get_gpu_usage()
        ram = SystemMonitor.get_ram_usage()
        self.performance_widget.layout().itemAt(0).widget().setText(
            f"CPU: {cpu}%\nGPU: {gpu}%\nRAM: {ram}%"
        )
        
        # Actualizar audio
        volume = AudioControl.get_current_volume()
        self.audio_widget.layout().itemAt(0).widget().setText(
            f"Volumen: {volume}%\nAplicación: {AudioControl.get_focused_app()}"
        )
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()
            
    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(event.globalPos() - self.offset)
            
    def mouseReleaseEvent(self, event):
        self.dragging = False