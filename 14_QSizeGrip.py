from PyQt5.QtWidgets import QApplication, QWidget, QGroupBox, QHBoxLayout, QVBoxLayout, QRadioButton, QSizeGrip
import sys
from PyQt5 import QtGui, QtCore


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Frameless Window"
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)

        vbox = QVBoxLayout()
        sizegrip = QSizeGrip(self)
        vbox.addWidget(sizegrip)

        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
