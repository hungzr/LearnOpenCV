from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QVBoxLayout, QApplication

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
