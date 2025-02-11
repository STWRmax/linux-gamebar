from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from modules.system_monitor import get_fps, get_ram_usage, get_gpu_usage, get_network_speed

class FloatingHUD(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_stats)
        self.timer.start(1000)  # Actualizar cada segundo

    def init_ui(self):
        layout = QVBoxLayout()
        self.fps_label = QLabel("FPS: ...")
        self.ram_label = QLabel("RAM: ...")
        self.gpu_label = QLabel("GPU: ...")
        self.network_label = QLabel("Network: ...")
        layout.addWidget(self.fps_label)
        layout.addWidget(self.ram_label)
        layout.addWidget(self.gpu_label)
        layout.addWidget(self.network_label)
        self.setLayout(layout)

    def update_stats(self):
        self.fps_label.setText(get_fps())
        self.ram_label.setText(get_ram_usage())
        self.gpu_label.setText(get_gpu_usage())
        self.network_label.setText(get_network_speed())