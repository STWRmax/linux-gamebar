from ui.floating_hud import FloatingHUD

app = QApplication(sys.argv)
window = MainWindow()
hud = FloatingHUD()
hud.show()
sys.exit(app.exec_())