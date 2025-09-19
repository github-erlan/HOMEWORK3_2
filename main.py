from PyQt6.QtWidgets import QApplication, QWidget
import sys

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Моё первое окно")
window.show()
sys.exit(app.exec())
