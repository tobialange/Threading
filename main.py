import sys
from PyQt6 import QtWidgets
from MainWindow import MainWindow


app = QtWidgets.QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
sys.exit(app.exec())