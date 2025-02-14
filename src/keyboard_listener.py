import keyboard
from src.ui.main_window import GameBarWindow

class HotkeyManager:
    def __init__(self):
        self.gamebar = GameBarWindow()
        keyboard.add_hotkey('ctrl+alt+g', self.toggle_gamebar)
        
    def toggle_gamebar(self):
        self.gamebar.setVisible(not self.gamebar.isVisible())
        
    def run(self):
        keyboard.wait()  # Mantiene el script activo