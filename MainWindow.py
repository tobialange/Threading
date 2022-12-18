from PyQt6.QtWidgets import QMainWindow
from Widget import Widget


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setCentralWidget(Widget(self))